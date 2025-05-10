import gradio as gr

def create_chatbot_interface(chatbot):
    def generate_response(user_input):
        return chatbot.chat(user_input)

    with gr.Blocks() as app:
        with gr.Row():
            text_input = gr.Textbox(label="Your Message", placeholder="Enter your message and press ENTER")

        output_area = gr.Textbox(label="Chatbot Response", interactive=False, lines=10)

        text_input.submit(generate_response, inputs=text_input, outputs=output_area)

    return app