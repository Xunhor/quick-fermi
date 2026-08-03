import dotenv from 'dotenv';
dotenv.config();

export const config = {
    // Aqui você pode colocar o link do seu Calendly ou Google Calendar
    calendlyLink: process.env.CALENDLY_LINK || "https://calendly.com/bem-vindo/30min",
    
    // Simula um delay humano ao digitar (em milissegundos)
    typingDelay: 3000, 
    
    // Evita que o bot responda a mesma pessoa 2 vezes seguidas na mesma sessão
    processedNumbers: new Set<string>()
};
