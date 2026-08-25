// Configuração Central do Menu
// Altere os nomes dos botões do menu aqui. As alterações vão refletir em todas as páginas (index e sobre).
const MENU_CONFIG = [
    { id: "modelos", name: "Modelos" },
    { id: "como-funciona", name: "Como Funciona" },
    { id: "planos", name: "Planos" },
    { id: "comparativo", name: "Comparativo" },
    { id: "sobre", name: "Sobre Nós" },
    { id: "faq", name: "FAQ" }
];

document.addEventListener("DOMContentLoaded", () => {
    // Procura todos os links do menu que têm o atributo data-menu-id
    const navLinks = document.querySelectorAll('.nav-links a[data-menu-id]');
    
    navLinks.forEach(link => {
        const menuId = link.getAttribute('data-menu-id');
        // Encontra a configuração correspondente no array central
        const configItem = MENU_CONFIG.find(item => item.id === menuId);
        
        if (configItem) {
            // Atualiza o texto visível do link com o nome centralizado
            link.textContent = configItem.name;
        }
    });
});
