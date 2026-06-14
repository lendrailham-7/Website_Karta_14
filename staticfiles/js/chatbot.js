console.log(sendMessageUrl);
console.log(csrfToken);
window.sendMessage = async function () {


const input = document.getElementById(
    'message-input'
);

const chatBox = document.getElementById(
    'chat-box'
);

const message = input.value;

if (!message.trim()) {

    return;

}

// Bubble user
chatBox.innerHTML += `

<div class="d-flex justify-content-end mb-3">

    <div class="chat-user">

        ${message}

    </div>

</div>

`;

chatBox.scrollTop = chatBox.scrollHeight;

input.value = '';

// Bubble typing
const typingId = Date.now();

chatBox.innerHTML += `

<div
    class="d-flex justify-content-start mb-3"
    id="typing-${typingId}"
>

    <div class="chat-bot typing-bubble">

        <span class="typing-dot"></span>

        <span class="typing-dot"></span>

        <span class="typing-dot"></span>

    </div>

</div>

`;

chatBox.scrollTop = chatBox.scrollHeight;

// Fetch ke backend
const response = await fetch(

    sendMessageUrl,

    {

        method: 'POST',

        headers: {

            'Content-Type': 'application/json',

            'X-CSRFToken': csrfToken

        },

        body: JSON.stringify({

            message: message

        })

    }

);

const data = await response.json();

// Jeda natural
await new Promise(

    resolve => setTimeout(

        resolve,

        1200

    )

);

// Hapus typing
document.getElementById(

    `typing-${typingId}`

)?.remove();
const formattedReply = data.reply

    .replace(/\n/g, "<br>")

    .replace(
        /(\d+\.)/g,
        "<br>$1"
    )

    .replace(
        /^-\s/gm,
        "• "
    );
    
// Bubble bot
chatBox.innerHTML += `

<div class="d-flex justify-content-start mb-3">

    <div class="chat-bot">

        ${formattedReply}

    </div>

</div>

`;

chatBox.scrollTop = chatBox.scrollHeight;


}

document.addEventListener(

    "DOMContentLoaded",

    function () {

        const input = document.getElementById(
            "message-input"
        );

        input.addEventListener(

            "keypress",

            function (event) {

                if (

                    event.key === "Enter"

                ) {

                    event.preventDefault();

                    sendMessage();

                }

            }

        );

    }

);