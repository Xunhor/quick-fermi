import { Message } from 'whatsapp-web.js';
import { config } from '../config/env';

/**
 * Função para extrair dados da string padrão gerada pelo site
 * Exemplo de texto gerado pelo site:
 * Olá! Sou da *Acme Corp*.
 * Nossa operação hoje funciona com:
 * _👉 Processos manuais e planilhas_
 *
 * Mas o que mais nos incomoda é:
 * _🚨 Falta de controle (dados espalhados)_
 *
 * Gostaria de agendar o diagnóstico técnico.
 */
function parseLeadMessage(body: string) {
    try {
        // Expressões regulares leves para extrair o nome e a dor
        const empresaMatch = body.match(/Sou da \*(.*?)\*/);
        const desafioMatch = body.match(/-> (.*?)_/g); // Pega todas as ocorrências de '-> texto_'
        
        const empresa = empresaMatch ? empresaMatch[1] : "sua empresa";
        // O desafio está na segunda ocorrência do '->'
        const desafio = desafioMatch && desafioMatch.length >= 2 ? desafioMatch[1].replace('-> ', '').replace('_', '') : "seus desafios atuais";
        
        return { isLead: true, empresa, desafio };
    } catch (e) {
        return { isLead: false, empresa: "", desafio: "" };
    }
}

/**
 * Utilitário para criar um delay (Promise)
 */
const delay = (ms: number) => new Promise(res => setTimeout(res, ms));

/**
 * Processador principal de mensagens
 */
export async function handleMessage(msg: Message) {
    // Ignorar mensagens de grupos, encaminhadas ou status (permitindo 'fromMe' para você poder testar consigo mesmo)
    if (msg.isForwarded || msg.isStatus) return;

    let chat;
    try {
        chat = await msg.getChat();
        if (chat && chat.isGroup) return;
    } catch (e) {
        // Ignora erros ao tentar pegar o chat de mensagens "para si mesmo"
    }

    const body = msg.body;
    console.log(`[DEBUG] Mensagem detectada: ${body.substring(0, 50)}...`);

    // Verificar se a mensagem possui o "Padrão de Automação" gerado pelo site
    if (body.includes("Olá! Sou da") && body.includes("Gostaria de agendar o diagnóstico técnico")) {
        const remoteNumber = msg.from;

        // Verifica se já processamos esse número nesta sessão (para evitar loop)
        if (config.processedNumbers.has(remoteNumber)) {
            return;
        }

        const leadData = parseLeadMessage(body);
        
        // Marca como processado
        config.processedNumbers.add(remoteNumber);

        console.log(`[LEAD RECEBIDO] Empresa: ${leadData.empresa} | Dor: ${leadData.desafio}`);

        // Simulando digitação humana
        if (chat) await chat.sendStateTyping();
        await delay(config.typingDelay);

        // Resposta 1 (Empatia e Autoridade)
        const resposta1 = `Olá! Recebi as informações da *${leadData.empresa}*.\n\nEntendi perfeitamente. Lidar com *${leadData.desafio.toLowerCase()}* trava o crescimento de qualquer operação.\n\nA boa notícia é que resolver gargalos operacionais usando Engenharia de Software é exatamente a nossa especialidade na Boomo. 🚀`;
        await msg.reply(resposta1);

        // Simulando digitação para a segunda mensagem
        if (chat) await chat.sendStateTyping();
        await delay(config.typingDelay + 1000);

        // Resposta 2 (Call to Action para Agenda)
        const resposta2 = `Para o nosso diagnóstico técnico ser bem assertivo, por favor, escolha o melhor horário na agenda do nosso Engenheiro Chefe aqui:\n\n📅 *Agendar Diagnóstico:* ${config.calendlyLink}\n\nAssim que reservar, me avise por aqui!`;
        if (chat) {
            await chat.sendMessage(resposta2);
        } else {
            await msg.reply(resposta2);
        }
    }
}
