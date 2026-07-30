// Simples navegação suave (Smooth Scroll) para links internos
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

/* =========================================================
   LÓGICA DO MOTOR DE AGENDAMENTO (WHATSAPP MVP)
========================================================= */
const WHATSAPP_NUMBER = "559191302044"; // Número de teste fornecido pelo usuário

// Estado do agendamento
let selectedDate = null;
let selectedTime = null;

// Elementos da DOM
const calendarDates = document.getElementById('calendar-dates');
const timeSlotsContainer = document.getElementById('time-slots-container');
const step2 = document.getElementById('step-2');
const step3 = document.getElementById('step-3');
const patientNameInput = document.getElementById('patient-name');
const parentNameInput = document.getElementById('parent-name');
const btnFinishBooking = document.getElementById('btn-finish-booking');

// 1. Gerar o calendário (Mês atual de exemplo)
function renderCalendar() {
    // Simulando um mês de 31 dias, começando na terça-feira (exemplo)
    let html = '';
    // Espaços vazios
    for(let i=0; i<2; i++) {
        html += '<span class="empty"></span>';
    }
    // Dias
    for(let i=1; i<=31; i++) {
        html += `<span>${i}</span>`;
    }
    calendarDates.innerHTML = html;

    // Adicionar eventos de clique
    const days = calendarDates.querySelectorAll('span:not(.empty)');
    days.forEach(day => {
        day.addEventListener('click', () => {
            // Remover seleção anterior
            days.forEach(d => d.classList.remove('selected'));
            day.classList.add('selected');
            
            selectedDate = `${day.innerText} de Agosto`;
            unlockStep2();
        });
    });
}

// 2. Destravar Horários
function unlockStep2() {
    step2.classList.remove('disabled');
    step2.classList.add('active');
    
    // Gerar horários fictícios
    const times = ['09:00', '09:30', '10:00', '14:00', '14:30', '15:00', '16:00'];
    let html = '';
    times.forEach(t => {
        html += `<div class="time-slot">${t}</div>`;
    });
    timeSlotsContainer.innerHTML = html;

    // Adicionar eventos
    const slots = timeSlotsContainer.querySelectorAll('.time-slot');
    slots.forEach(slot => {
        slot.addEventListener('click', () => {
            slots.forEach(s => s.classList.remove('selected'));
            slot.classList.add('selected');
            
            selectedTime = slot.innerText;
            unlockStep3();
        });
    });
}

// 3. Destravar Formulário
function unlockStep3() {
    step3.classList.remove('disabled');
    step3.classList.add('active');
    
    patientNameInput.disabled = false;
    parentNameInput.disabled = false;
    btnFinishBooking.disabled = false;
}

// 4. Finalizar e abrir WhatsApp
btnFinishBooking.addEventListener('click', () => {
    const pName = patientNameInput.value.trim();
    const rName = parentNameInput.value.trim();

    if(!pName || !rName) {
        alert("Por favor, preencha os nomes para continuar.");
        return;
    }

    const mensagem = `Olá! Gostaria de solicitar um agendamento na Clínica Sorriso Infantil.\n\n*Data:* ${selectedDate}\n*Horário:* ${selectedTime}\n*Paciente:* ${pName}\n*Responsável:* ${rName}\n\nEste horário está disponível?`;
    
    const encodedMessage = encodeURIComponent(mensagem);
    const whatsappUrl = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodedMessage}`;
    
    window.open(whatsappUrl, '_blank');
});

// Iniciar sistema
renderCalendar();
