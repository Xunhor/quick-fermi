import { Client, LocalAuth } from 'whatsapp-web.js';
import qrcode from 'qrcode-terminal';
import { handleMessage } from '../services/messageHandler';
import fs from 'fs';

// Função para encontrar o Chrome/Edge instalado no Windows
const getBrowserPath = () => {
    const paths = [
        'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
        'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
        'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe'
    ];
    for (const p of paths) {
        if (fs.existsSync(p)) return p;
    }
    return undefined; // Se não achar, deixa o puppeteer tentar o default (que está dando erro)
};

export const startWhatsAppClient = () => {
    console.log('🔄 Inicializando Cliente WhatsApp...');

    // Utiliza autenticação local para não precisar ler o QR Code toda vez que reiniciar
    const client = new Client({
        authStrategy: new LocalAuth(),
        puppeteer: {
            executablePath: getBrowserPath(),
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        }
    });

    // Quando precisa de autenticação, gera o QR Code no terminal
    client.on('qr', (qr) => {
        console.log('\n=========================================');
        console.log('📱 ESCANEIE O QR CODE ABAIXO NO SEU WHATSAPP');
        console.log('=========================================\n');
        qrcode.generate(qr, { small: true });
    });

    // Quando conectar com sucesso
    client.on('ready', () => {
        console.log('\n✅ Bot da Fundação está ONLINE e pronto para receber Leads!\n');
    });

    // Escutador de mensagens (usando message_create para pegar as suas próprias mensagens de teste também)
    client.on('message_create', async (msg) => {
        await handleMessage(msg);
    });

    // Tratamento de erros de autenticação
    client.on('auth_failure', msg => {
        console.error('❌ Falha na autenticação do WhatsApp:', msg);
    });

    // Inicia o cliente
    client.initialize();
};
