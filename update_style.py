css_to_add = '''
  /* --- PREMIUM TECH AESTHETIC --- */
  
  /* 1. Subtle Dark Mode Noise Texture */
  html.dark-theme::after {
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 9999;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.08'/%3E%3C/svg%3E");
      background-repeat: repeat;
      opacity: 0.25;
  }
  
  /* 2. Premium Glow Hover on Cards */
  .price-card, .timeline-step-card, .inclusive-item {
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease;
  }
  
  html.dark-theme .price-card:hover, 
  html.dark-theme .timeline-step-card:hover, 
  html.dark-theme .inclusive-item:hover {
      border-color: rgba(34, 211, 238, 0.3);
      box-shadow: 0 10px 40px -10px rgba(34, 211, 238, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.15);
      transform: translateY(-4px);
  }
  
  /* 3. Refined Glassmorphism Badge */
  html.dark-theme .featured-badge {
      background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(255,255,255,0.8));
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255,255,255,0.4);
      color: #000;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
  }
'''

with open('css/desktop/style.css', 'a', encoding='utf-8') as f:
    f.write(css_to_add)

print("Done style.css")
