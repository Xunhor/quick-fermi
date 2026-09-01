import re

with open('test_sasha_webgl.html', 'r', encoding='utf-8') as f:
    test_html = f.read()

# Extract script content from test_sasha_webgl.html
script_content = re.search(r'<script>(.*?)</script>', test_html, re.DOTALL).group(1)

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# In index.html, find from "// SASHA MARTYNCHUK STYLE INFINITE 3D GRID ENGINE" to "// Preview Modal Logic"
pattern = r'// SASHA MARTYNCHUK STYLE INFINITE 3D GRID ENGINE.*?(?=\s*// Preview Modal Logic)'

webgl_integration = """// SASHA MARTYNCHUK NATIVE WEBGL 2.0 SPHERICAL DOME ENGINE
        const TEX_SIZE = 512;
        const _t = 10;
        const Eo = 0.06, To = 0.028, Ro = 0.2, xo = 0.09, bo = 0.12, Ae = 5, Ao = 0, wo = 1, we = 0, Mo = 0.25, So = 132, Lo = 340, Me = 2600 * 1400;
        const clamp = (val, min, max) => Math.min(max, Math.max(min, val));

        function hashCoord(x, y) {
            let e = Math.imul(x, 73856093) ^ Math.imul(y, 19349663);
            e ^= e >>> 13;
            e = Math.imul(e, 1274126177);
            return ((e ^ (e >>> 16)) >>> 0);
        }

        const vsGrid = `#version 300 es
precision highp float;

in vec2 aUV;      
in vec2 aCell;    
in float aLayer;  
in float aLift;   

uniform vec2  uOffset;
uniform vec2  uCell;
uniform vec2  uMedia;
uniform float uR;
uniform float uPersp;   
uniform float uCamZ;    
uniform vec2  uHalfViewport;
uniform float uReveal;

out vec2  vUV;
out float vLayer;
out float vShade;
out float vLift;
out float vEnter;
out vec2  vParallax;

vec3 surface(vec2 arc) {
  vec2 ang = arc / uR;
  return vec3(uR * sin(ang.x),
              uR * sin(ang.y),
              uR * (2.0 - cos(ang.x) - cos(ang.y)));
}

void main() {
  vec2 centre = aCell * uCell - uOffset;
  vec2 local  = (aUV - 0.5) * uMedia * (1.0 + aLift * 0.05);
  vec3 P      = surface(centre + local);

  vec2 ang = centre / uR;
  float facing = cos(ang.x) * cos(ang.y);

  float st = sin(ang.x), ct = cos(ang.x);
  float sp = sin(ang.y), cp = cos(ang.y);
  vec3 T = vec3(ct, 0.0, st);
  vec3 B = vec3(-sp * st, cp, sp * ct);
  vec3 N = vec3(-st * cp, -sp, ct * cp);

  vec3 toCam = normalize(vec3(0.0, 0.0, uCamZ) - P);
  float nd = max(dot(toCam, N), 0.25);
  vParallax = vec2(dot(toCam, T), dot(toCam, B)) / nd;

  P.z += aLift * uCell.x * 0.12;

  float d = length(centre / uCell);
  float t = clamp(uReveal * 1.9 - d * 0.14, 0.0, 1.0);
  float e = 1.0 - pow(1.0 - t, 3.0);
  P.z -= (1.0 - e) * uPersp * 1.8;

  vec3 V = vec3(P.x, -P.y, P.z - uCamZ);
  float n = uPersp * 0.05;
  float f = uPersp * 5.0;

  gl_Position = vec4(
    uPersp * V.x / uHalfViewport.x,
    uPersp * V.y / uHalfViewport.y,
    ((f + n) * V.z + 2.0 * f * n) / (n - f),
    -V.z
  );

  vUV    = aUV;
  vLayer = aLayer;
  vShade = clamp((1.0 - facing) * 1.5, 0.0, 0.7);
  vLift  = aLift * e;
  vEnter = e;
}
`;

        const fsGrid = `#version 300 es
precision highp float;
precision highp sampler2DArray;

in vec2  vUV;
in float vLayer;
in float vShade;
in float vLift;
in float vEnter;
in vec2  vParallax;

uniform sampler2DArray uTex;
uniform vec2  uMediaPx;
uniform float uRadius;
uniform float uDepth;  
uniform float uZoom;   
uniform vec2  uDrag;   

out vec4 fragColor;

void main() {
  vec2 halfSize = uMediaPx * 0.5;
  vec2 q = abs((vUV - 0.5) * uMediaPx) - (halfSize - uRadius);
  float d = length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - uRadius;
  float cover = 1.0 - smoothstep(-1.0, 1.0, d);

  float lim = (1.0 - uZoom) * 0.5;
  vec2 off = clamp((vParallax * uDepth + uDrag) / uMediaPx, -lim, lim);
  vec2 uv = 0.5 + (vUV - 0.5) * uZoom - off;

  vec3 c = texture(uTex, vec3(uv, vLayer)).rgb;

  c *= 1.0 - vShade * 0.55;

  float l = dot(c, vec3(0.299, 0.587, 0.114));
  c = mix(vec3(l), c, 1.0 - vShade * 0.45);

  fragColor = vec4(c * vEnter, cover);
}
`;

        const vsPost = `#version 300 es
precision highp float;

void main() {
  vec2 p = vec2((gl_VertexID << 1) & 2, gl_VertexID & 2);
  gl_Position = vec4(p * 2.0 - 1.0, 0.0, 1.0);
}
`;

        const fsPost = `#version 300 es
precision highp float;

uniform sampler2D uScene;
uniform vec2  uResolution;
uniform float uTime;

out vec4 fragColor;

void main() {
  vec2 uv = gl_FragCoord.xy / uResolution;
  vec2 c  = uv - 0.5;

  vec3 col = texture(uScene, uv).rgb;
  col *= smoothstep(1.25, 0.30, length(c) * 1.5);

  float n = fract(sin(dot(gl_FragCoord.xy + fract(uTime) * 91.7, vec2(12.9898, 78.233))) * 43758.5453);
  col += (n - 0.5) * 0.030;

  fragColor = vec4(col, 1.0);
}
`;

        function createShader(gl, type, source) {
            const s = gl.createShader(type);
            gl.shaderSource(s, source);
            gl.compileShader(s);
            if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
                throw new Error(gl.getShaderInfoLog(s) || 'shader compile failed');
            }
            return s;
        }

        function createProgram(gl, vs, fs) {
            const p = gl.createProgram();
            gl.attachShader(p, createShader(gl, gl.VERTEX_SHADER, vs));
            gl.attachShader(p, createShader(gl, gl.FRAGMENT_SHADER, fs));
            gl.linkProgram(p);
            if (!gl.getProgramParameter(p, gl.LINK_STATUS)) {
                throw new Error(gl.getProgramInfoLog(p) || 'program link failed');
            }
            return p;
        }

        function getUniforms(gl, prog) {
            const u = {};
            const count = gl.getProgramParameter(prog, gl.ACTIVE_UNIFORMS);
            for (let i = 0; i < count; i++) {
                const name = gl.getActiveUniform(prog, i).name.replace(/\\[0\\]$/, '');
                u[name] = gl.getUniformLocation(prog, name);
            }
            return u;
        }

        class SashaStage {
            constructor(canvas, items) {
                this.canvas = canvas;
                this.items = items;
                const gl = canvas.getContext('webgl2', {
                    antialias: false,
                    alpha: false,
                    depth: false,
                    powerPreference: 'high-performance'
                });
                if (!gl) throw new Error('WebGL2 unavailable');
                this.gl = gl;

                this.pos = { x: 0, y: 0 };
                this.target = { x: 0, y: 0 };
                this.velocity = { x: 0, y: 0 };
                this.smoothVel = { x: 0, y: 0 };
                this.pointer = { x: -1e5, y: -1e5 };
                this.smoothPointer = { x: -1e5, y: -1e5 };
                this.dragging = false;
                this.hold = 0;
                this.pointerId = null;
                this.revealT = 1;
                this.revealing = false;
                this.parallax = 1;
                this.camZ = 0;
                this.depthCull = 0.28;

                this.gridProg = createProgram(gl, vsGrid, fsGrid);
                this.gridU = getUniforms(gl, this.gridProg);
                this.postProg = createProgram(gl, vsPost, fsPost);
                this.postU = getUniforms(gl, this.postProg);

                this._buildPatch();
                this._buildTexture();
                this._bind();
                this.measure();
                this.lastTime = performance.now();
                this._tick = this._tick.bind(this);
                requestAnimationFrame(this._tick);
            }

            _buildPatch() {
                const gl = this.gl;
                const verts = [];
                for (let h = 0; h <= _t; h++) {
                    for (let d = 0; d <= _t; d++) {
                        verts.push(d / _t, h / _t);
                    }
                }
                const idxs = [];
                const r = _t + 1;
                for (let h = 0; h < _t; h++) {
                    for (let d = 0; d < _t; d++) {
                        const n = h * r + d;
                        idxs.push(n, n + 1, n + r, n + 1, n + r + 1, n + r);
                    }
                }
                this.indexCount = idxs.length;
                this.vao = gl.createVertexArray();
                gl.bindVertexArray(this.vao);

                const vBuf = gl.createBuffer();
                gl.bindBuffer(gl.ARRAY_BUFFER, vBuf);
                gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(verts), gl.STATIC_DRAW);
                const aUV = gl.getAttribLocation(this.gridProg, 'aUV');
                gl.enableVertexAttribArray(aUV);
                gl.vertexAttribPointer(aUV, 2, gl.FLOAT, false, 0, 0);

                const iBuf = gl.createBuffer();
                gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, iBuf);
                gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(idxs), gl.STATIC_DRAW);

                this.instBuf = gl.createBuffer();
                gl.bindBuffer(gl.ARRAY_BUFFER, this.instBuf);
                const attrs = [['aCell', 2, 0], ['aLayer', 1, 8], ['aLift', 1, 12]];
                for (const [name, size, offset] of attrs) {
                    const loc = gl.getAttribLocation(this.gridProg, name);
                    gl.enableVertexAttribArray(loc);
                    gl.vertexAttribPointer(loc, size, gl.FLOAT, false, 16, offset);
                    gl.vertexAttribDivisor(loc, 1);
                }
                gl.bindVertexArray(null);
            }

            _buildTexture() {
                const gl = this.gl;
                const count = this.items.length;
                const levels = Math.floor(Math.log2(TEX_SIZE)) + 1;
                const tex = gl.createTexture();
                gl.bindTexture(gl.TEXTURE_2D_ARRAY, tex);
                gl.texStorage3D(gl.TEXTURE_2D_ARRAY, levels, gl.RGBA8, TEX_SIZE, TEX_SIZE, count);
                gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false);

                for (let c = 0; c < count; c++) {
                    if (this.items[c].canvas) {
                        gl.texSubImage3D(gl.TEXTURE_2D_ARRAY, 0, 0, 0, c, TEX_SIZE, TEX_SIZE, 1, gl.RGBA, gl.UNSIGNED_BYTE, this.items[c].canvas);
                    }
                }
                gl.generateMipmap(gl.TEXTURE_2D_ARRAY);
                gl.texParameteri(gl.TEXTURE_2D_ARRAY, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR);
                gl.texParameteri(gl.TEXTURE_2D_ARRAY, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
                gl.texParameteri(gl.TEXTURE_2D_ARRAY, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
                gl.texParameteri(gl.TEXTURE_2D_ARRAY, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);

                const ext = gl.getExtension('EXT_texture_filter_anisotropic');
                if (ext) {
                    gl.texParameterf(gl.TEXTURE_2D_ARRAY, ext.TEXTURE_MAX_ANISOTROPY_EXT, 8);
                }
                this.tex = tex;
            }

            measure() {
                const w = this.canvas.clientWidth;
                const h = this.canvas.clientHeight;
                this.vw = w;
                this.vh = h;
                const dpr = Math.min(window.devicePixelRatio || 1, 2);
                this.dw = Math.round(w * dpr);
                this.dh = Math.round(h * dpr);
                this.canvas.width = this.dw;
                this.canvas.height = this.dh;

                const T = Math.round(clamp(Mo * Math.sqrt(w * h), So, Lo));
                const pad = Math.round(T * Eo);
                this.cell = T;
                this.media = T - pad * 2;
                this.radius = Math.max(2, T * To);

                const base = Math.max(w, h * 0.72);
                const A = clamp((base - 420) / 1020, 0, 1);
                this.R = base * (1.18 + (0.94 - 1.18) * A);
                this.persp = this.R * (0.85 + (0.65 - 0.85) * A);
                this.camZ = this.persp;

                const P = this._solveArc(w * 0.62);
                const O = this._solveArc(h * 0.62);
                this.cols = Math.min(27, Math.ceil((P / T) * 2) + Ae);
                this.rows = Math.min(19, Math.ceil((O / T) * 2) + Ae);
                if (this.cols % 2 === 0) this.cols++;
                if (this.rows % 2 === 0) this.rows++;

                this.instances = new Float32Array(this.cols * this.rows * 4);
                this._buildTargets();
            }

            _solveArc(target) {
                const { R, persp } = this;
                const maxAng = Math.acos(clamp(1 - (persp * 0.8) / R, -1, 1));
                let low = 0, high = maxAng;
                for (let i = 0; i < 36; i++) {
                    const mid = (low + high) / 2;
                    if ((R * Math.sin(mid) * persp) / (persp - R * (1 - Math.cos(mid))) < target) {
                        low = mid;
                    } else {
                        high = mid;
                    }
                }
                return R * low;
            }

            _buildTargets() {
                const gl = this.gl;
                const { dw, dh } = this;
                if (this.fboMS) {
                    gl.deleteFramebuffer(this.fboMS);
                    gl.deleteRenderbuffer(this.rbColor);
                    gl.deleteRenderbuffer(this.rbDepth);
                    gl.deleteFramebuffer(this.fboResolve);
                    gl.deleteTexture(this.texResolve);
                }
                this.rbColor = gl.createRenderbuffer();
                gl.bindRenderbuffer(gl.RENDERBUFFER, this.rbColor);
                gl.renderbufferStorageMultisample(gl.RENDERBUFFER, 4, gl.RGBA8, dw, dh);

                this.rbDepth = gl.createRenderbuffer();
                gl.bindRenderbuffer(gl.RENDERBUFFER, this.rbDepth);
                gl.renderbufferStorageMultisample(gl.RENDERBUFFER, 4, gl.DEPTH_COMPONENT24, dw, dh);

                this.fboMS = gl.createFramebuffer();
                gl.bindFramebuffer(gl.FRAMEBUFFER, this.fboMS);
                gl.framebufferRenderbuffer(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.RENDERBUFFER, this.rbColor);
                gl.framebufferRenderbuffer(gl.FRAMEBUFFER, gl.DEPTH_ATTACHMENT, gl.RENDERBUFFER, this.rbDepth);

                this.texResolve = gl.createTexture();
                gl.bindTexture(gl.TEXTURE_2D, this.texResolve);
                gl.texStorage2D(gl.TEXTURE_2D, 1, gl.RGBA8, dw, dh);
                gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
                gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);

                this.fboResolve = gl.createFramebuffer();
                gl.bindFramebuffer(gl.FRAMEBUFFER, this.fboResolve);
                gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, this.texResolve, 0);
                gl.bindFramebuffer(gl.FRAMEBUFFER, null);
            }

            _bind() {
                const canvas = this.canvas;
                canvas.addEventListener('pointerdown', (e) => {
                    if (e.button === 0) {
                        this.dragging = true;
                        this.pointerId = e.pointerId;
                        this.last = { x: e.clientX, y: e.clientY };
                        this.velocity.x = this.velocity.y = 0;
                        document.body.classList.add('is-dragging');
                        if (e.pointerType !== 'touch') canvas.setPointerCapture(e.pointerId);
                    }
                });

                window.addEventListener('pointermove', (e) => {
                    this.pointer.x = e.clientX;
                    this.pointer.y = e.clientY;
                    if (!this.dragging || e.pointerId !== this.pointerId) return;
                    const dx = e.clientX - this.last.x;
                    const dy = e.clientY - this.last.y;
                    this.last = { x: e.clientX, y: e.clientY };
                    const c = Math.max(this.camZ, this.persp * 0.02) / this.persp;
                    this.target.x -= dx * c;
                    this.target.y -= dy * c;
                    this.velocity.x = dx * c;
                    this.velocity.y = dy * c;
                }, { passive: true });

                const onUp = (e) => {
                    if (!this.dragging || (e && e.pointerId !== this.pointerId)) return;
                    this.dragging = false;
                    document.body.classList.remove('is-dragging');
                    this.target.x -= this.velocity.x * 14;
                    this.target.y -= this.velocity.y * 14;
                    this.velocity.x = 0;
                    this.velocity.y = 0;
                };
                window.addEventListener('pointerup', onUp);
                window.addEventListener('pointercancel', onUp);
            }

            get drawR() { return this.R * (1 - xo * this.hold); }
            get drawCamZ() { return this.camZ * (1 + Ro * this.hold); }

            pick(t, e) {
                const { cell: o, persp: r, pos: i, media: c } = this;
                const u = this.drawR, l = this.drawCamZ;
                const h = this.canvas.getBoundingClientRect();
                const d = t - h.left - this.vw / 2;
                const n = e - h.top - this.vh / 2;
                const f = Math.round(i.x / o);
                const v = Math.round(i.y / o);
                const m = (this.cols - 1) / 2;
                const T = (this.rows - 1) / 2;
                const w = this.items.length;
                let _ = null;
                for (let A = 0; A < this.rows; A++) {
                    for (let M = 0; M < this.cols; M++) {
                        const P = f + M - m;
                        const O = v + A - T;
                        const U = (P * o - i.x) / u;
                        const W = (O * o - i.y) / u;
                        const y = Math.cos(U), S = Math.cos(W);
                        const G = l - u * (2 - y - S);
                        if (y * S < 0.45 || G < r * this.depthCull) continue;
                        const p = r / G;
                        const g = u * Math.sin(U) * p;
                        const C = u * Math.sin(W) * p;
                        const F = c * p / 2;
                        if (Math.abs(d - g) > F || Math.abs(n - C) > F) continue;
                        if (!_ || _.scale < p) {
                            _ = { index: hashCoord(P, O) % w, sx: g, sy: C, size: F * 2, scale: p };
                        }
                    }
                }
                return _ ? { index: _.index, sx: _.sx + this.vw / 2 + h.left, sy: _.sy + this.vh / 2 + h.top, size: _.size } : null;
            }

            _pack() {
                const { cell: t, persp: e, pos: o } = this;
                const r = this.drawR;
                const i = this.drawCamZ;
                const c = Math.round(o.x / t);
                const u = Math.round(o.y / t);
                const l = (this.cols - 1) / 2;
                const h = (this.rows - 1) / 2;
                const d = this.items.length;
                const n = this.instances;
                const f = this.smoothPointer.x - this.vw / 2;
                const v = this.smoothPointer.y - this.vh / 2;
                const m = t * 1.5;
                let count = 0;

                for (let w = 0; w < this.rows; w++) {
                    for (let _ = 0; _ < this.cols; _++) {
                        const A = c + _ - l;
                        const M = u + w - h;
                        const P = A * t - o.x;
                        const O = M * t - o.y;
                        const U = P / r;
                        const W = O / r;
                        const y = Math.cos(U);
                        const S = Math.cos(W);
                        const G = r * (2 - y - S);
                        const p = i - G;
                        if (y * S < 0.45 || p < e * this.depthCull) continue;
                        const g = e / p;
                        const C = r * Math.sin(U) * g;
                        const F = r * Math.sin(W) * g;
                        const H = t * g;
                        if (Math.abs(C) > this.vw * 0.5 + H || Math.abs(F) > this.vh * 0.5 + H) continue;

                        let Z = 1 - Math.hypot(C - f, F - v) / m;
                        Z = Z <= 0 ? 0 : Z * Z * (3 - 2 * Z);
                        const idx = count * 4;
                        n[idx] = A;
                        n[idx + 1] = M;
                        n[idx + 2] = hashCoord(A, M) % d;
                        n[idx + 3] = Z;
                        count++;
                    }
                }
                return count;
            }

            _draw(time) {
                const gl = this.gl;
                const count = this._pack();

                gl.bindBuffer(gl.ARRAY_BUFFER, this.instBuf);
                gl.bufferData(gl.ARRAY_BUFFER, this.instances, gl.DYNAMIC_DRAW);
                gl.bindFramebuffer(gl.FRAMEBUFFER, this.fboMS);
                gl.viewport(0, 0, this.dw, this.dh);
                gl.clearColor(0, 0, 0, 1);
                gl.clearDepth(1);
                gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

                gl.enable(gl.DEPTH_TEST);
                gl.depthFunc(gl.LEQUAL);
                gl.enable(gl.SAMPLE_ALPHA_TO_COVERAGE);

                gl.useProgram(this.gridProg);
                gl.bindVertexArray(this.vao);
                gl.activeTexture(gl.TEXTURE0);
                gl.bindTexture(gl.TEXTURE_2D_ARRAY, this.tex);

                const u = this.gridU;
                gl.uniform1i(u.uTex, 0);
                gl.uniform2f(u.uOffset, this.pos.x, this.pos.y);
                gl.uniform2f(u.uCell, this.cell, this.cell);
                gl.uniform2f(u.uMedia, this.media, this.media);
                gl.uniform2f(u.uMediaPx, this.media, this.media);
                gl.uniform1f(u.uRadius, this.radius);
                gl.uniform1f(u.uZoom, wo);
                gl.uniform1f(u.uDepth, this.media * Ao * this.parallax);
                gl.uniform2f(u.uDrag, clamp(this.smoothVel.x * we, -this.media * 0.04, this.media * 0.04), clamp(this.smoothVel.y * we, -this.media * 0.04, this.media * 0.04));
                gl.uniform1f(u.uR, this.drawR);
                gl.uniform1f(u.uPersp, this.persp);
                gl.uniform1f(u.uCamZ, this.drawCamZ);
                gl.uniform2f(u.uHalfViewport, this.vw / 2, this.vh / 2);
                gl.uniform1f(u.uReveal, this.revealT);

                gl.drawElementsInstanced(gl.TRIANGLES, this.indexCount, gl.UNSIGNED_SHORT, 0, count);

                gl.disable(gl.SAMPLE_ALPHA_TO_COVERAGE);
                gl.bindVertexArray(null);
                gl.disable(gl.DEPTH_TEST);

                gl.bindFramebuffer(gl.READ_FRAMEBUFFER, this.fboMS);
                gl.bindFramebuffer(gl.DRAW_FRAMEBUFFER, this.fboResolve);
                gl.blitFramebuffer(0, 0, this.dw, this.dh, 0, 0, this.dw, this.dh, gl.COLOR_BUFFER_BIT, gl.LINEAR);

                gl.bindFramebuffer(gl.FRAMEBUFFER, null);
                gl.viewport(0, 0, this.dw, this.dh);
                gl.useProgram(this.postProg);
                gl.activeTexture(gl.TEXTURE0);
                gl.bindTexture(gl.TEXTURE_2D, this.texResolve);
                gl.uniform1i(this.postU.uScene, 0);
                gl.uniform2f(this.postU.uResolution, this.dw, this.dh);
                gl.uniform1f(this.postU.uTime, time * 0.001);
                gl.drawArrays(gl.TRIANGLES, 0, 3);
            }

            _tick(time) {
                const delta = Math.min(64, time - this.lastTime);
                this.lastTime = time;
                requestAnimationFrame(this._tick);

                this.hold += ((this.dragging ? 1 : 0) - this.hold) * (1 - Math.pow(1 - bo, delta / 16.667));
                const ease = this.dragging ? 0.26 : 0.075;
                const r = 1 - Math.pow(1 - ease, delta / 16.667);

                this.pos.x += (this.target.x - this.pos.x) * r;
                this.pos.y += (this.target.y - this.pos.y) * r;

                this.smoothPointer.x += (this.pointer.x - this.smoothPointer.x) * 0.15;
                this.smoothPointer.y += (this.pointer.y - this.smoothPointer.y) * 0.15;

                if (!this.dragging) {
                    this.target.x += 0.22;
                    this.target.y += 0.08;
                }

                this._draw(time);
            }
        }

        // Initialize WebGL Stage on Page Load
        window.addEventListener('DOMContentLoaded', async () => {
            const canvas = document.getElementById('stageGl');
            const activeModelTitle = document.getElementById('activeModelTitle');
            if (!canvas) return;

            const items = [];

            // Helper to draw luxury framed tile
            async function buildTileCanvas(cardData) {
                const c = document.createElement('canvas');
                c.width = TEX_SIZE;
                c.height = TEX_SIZE;
                const ctx = c.getContext('2d');

                // Background
                ctx.fillStyle = cardData.bg;
                ctx.fillRect(0, 0, TEX_SIZE, TEX_SIZE);

                // Inner Website Mockup
                try {
                    const img = new Image();
                    img.src = cardData.img;
                    await new Promise((res) => {
                        img.onload = res;
                        img.onerror = res;
                    });

                    if (img.width > 0) {
                        const pad = 24;
                        const innerW = TEX_SIZE - pad * 2;
                        const innerH = TEX_SIZE - pad * 2 - 48;

                        ctx.save();
                        ctx.beginPath();
                        ctx.roundRect(pad, pad, innerW, innerH, 16);
                        ctx.clip();
                        ctx.drawImage(img, 0, 0, img.width, img.height, pad, pad, innerW, innerH);
                        ctx.restore();

                        ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
                        ctx.lineWidth = 2;
                        ctx.beginPath();
                        ctx.roundRect(pad, pad, innerW, innerH, 16);
                        ctx.stroke();
                    }
                } catch(e) {}

                // Footer Text
                ctx.fillStyle = '#FFFFFF';
                ctx.font = '600 20px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
                ctx.fillText(cardData.title, 26, TEX_SIZE - 24);

                ctx.fillStyle = 'rgba(255, 255, 255, 0.55)';
                ctx.font = '500 15px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
                ctx.textAlign = 'right';
                ctx.fillText(cardData.niche.toUpperCase(), TEX_SIZE - 26, TEX_SIZE - 24);

                return c;
            }

            for (const tpl of templates) {
                const c = await buildTileCanvas(tpl);
                items.push({ canvas: c, data: tpl });
            }

            try {
                window.sasha = new SashaStage(canvas, items);
                
                // Click & Hover Events on Canvas
                let pointerDownPos = null;
                canvas.addEventListener('pointerdown', (e) => {
                    pointerDownPos = { x: e.clientX, y: e.clientY, time: performance.now() };
                });

                canvas.addEventListener('pointerup', (e) => {
                    if (!pointerDownPos) return;
                    const dx = Math.abs(e.clientX - pointerDownPos.x);
                    const dy = Math.abs(e.clientY - pointerDownPos.y);
                    const dt = performance.now() - pointerDownPos.time;
                    if (dx < 8 && dy < 8 && dt < 400) {
                        const hit = window.sasha?.pick(e.clientX, e.clientY);
                        if (hit && templates[hit.index]) {
                            const tpl = templates[hit.index];
                            openPreview(tpl.url, tpl.domain, tpl.title);
                        }
                    }
                });

                canvas.addEventListener('pointermove', (e) => {
                    const hit = window.sasha?.pick(e.clientX, e.clientY);
                    if (hit && templates[hit.index]) {
                        canvas.style.cursor = 'pointer';
                        const tpl = templates[hit.index];
                        if (activeModelTitle) {
                            activeModelTitle.textContent = `${tpl.title.toUpperCase()} • ${tpl.niche.toUpperCase()}`;
                            activeModelTitle.style.color = '#FFFFFF';
                        }
                    } else {
                        canvas.style.cursor = window.sasha?.dragging ? 'grabbing' : 'grab';
                        if (activeModelTitle) {
                            activeModelTitle.textContent = 'MODELOS DEMONSTRATIVOS REAIS';
                            activeModelTitle.style.color = 'var(--color-muted)';
                        }
                    }
                });

                window.addEventListener('resize', () => {
                    window.sasha?.measure();
                    updateModalIframeScale();
                });
            } catch (err) {
                console.error('WebGL 2 failed:', err);
            }
        });
"""

new_html = re.sub(pattern, webgl_integration, index_html, count=1, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully replaced with Sasha Martynchuk WebGL 2.0 engine in index.html!")
