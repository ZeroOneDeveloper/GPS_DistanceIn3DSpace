import gradio as gr

import math

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            latitudes1 = gr.Number(label="Latitude (위도)", info='-180 ~ 180')
            longitudes1 = gr.Number(label="Longitude (경도)", info='-90 ~ 90')
        with gr.Column():
            latitudes2 = gr.Number(label="Latitude (위도)", info='-180 ~ 180')
            longitudes2 = gr.Number(label="Longitude (경도)", info='-90 ~ 90')
    RunButton = gr.Button("Run")
    Distance = gr.Textbox(value="", label="Distance (m)")

    def EquirectangularApproximation(x1, y1, x2, y2):
        x = (x2 - x1) * math.cos(0.5 * (y2 + y1))
        y = y2 - y1
        d = math.sqrt(x ** 2 + y ** 2) * 6371e3
        return d

    RunButton.click(EquirectangularApproximation, inputs=[latitudes1, longitudes1, latitudes2, longitudes2], outputs=[Distance])

demo.launch(
    server_name='0.0.0.0',
    server_port=7878,
)
