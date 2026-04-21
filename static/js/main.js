(function () {
    // Mobile nav toggle
    const toggle = document.getElementById('navToggle');
    const links = document.getElementById('navLinks');
    if (toggle && links) {
        toggle.addEventListener('click', () => links.classList.toggle('open'));
    }

    // Floating chat widget
    const fab = document.getElementById('chatToggle');
    const panel = document.getElementById('chatPanel');
    const close = document.getElementById('chatClose');
    const log = document.getElementById('chatLog');
    const form = document.getElementById('chatForm');
    const input = document.getElementById('chatInput');
    if (!fab || !panel) return;

    const csrf = document.cookie.split('; ').find(r => r.startsWith('csrftoken='))?.split('=')[1];

    function openPanel() {
        panel.hidden = false;
        fab.setAttribute('aria-expanded', 'true');
        if (!log.dataset.initialized) {
            append('bot', { reply: "Hi there! I'm your travel assistant. Try: 'show flights', 'list hotels', or 'view packages'." });
            log.dataset.initialized = '1';
        }
        setTimeout(() => input && input.focus(), 100);
    }
    function closePanel() {
        panel.hidden = true;
        fab.setAttribute('aria-expanded', 'false');
    }
    fab.addEventListener('click', () => (panel.hidden ? openPanel() : closePanel()));
    if (close) close.addEventListener('click', closePanel);

    function append(role, data) {
        const el = document.createElement('div');
        el.className = 'msg msg-' + role;
        const bubble = document.createElement('div');
        bubble.className = 'bubble';
        const reply = (data.reply || data).toString().replace(/\n/g, '<br>');
        bubble.innerHTML = reply;
        if (data.items && data.items.length) {
            const list = document.createElement('div');
            list.className = 'chat-items';
            data.items.forEach(it => {
                list.insertAdjacentHTML('beforeend',
                    `<a href="${it.url}" class="chat-item"><strong>${it.title}</strong><span>${it.subtitle}</span><em>${it.meta}</em></a>`);
            });
            bubble.appendChild(list);
        }
        if (data.cta) {
            bubble.insertAdjacentHTML('beforeend',
                `<a class="btn btn-outline btn-sm mt-8" href="${data.cta.url}">${data.cta.label}</a>`);
        }
        el.appendChild(bubble);
        log.appendChild(el);
        log.scrollTop = log.scrollHeight;
    }

    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const text = input.value.trim();
            if (!text) return;
            append('user', { reply: text });
            input.value = '';
            try {
                const res = await fetch('/chatbot/api/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrf || '' },
                    body: JSON.stringify({ message: text })
                });
                const data = await res.json();
                append('bot', data);
            } catch (err) {
                append('bot', { reply: "Sorry, I couldn't reach the server. Please try again." });
            }
        });
    }
})();
