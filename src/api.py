from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import uvicorn

app = FastAPI()

# Load the model and tokenizer once when the application starts
model = GPT2LMHeadModel.from_pretrained('/mnt/d/Workspace/Prodigy_InfoTech_Internship/task1-Text_Genration_with_gpt2/model/checkpoint-30000/')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-medium')
tokenizer.pad_token = tokenizer.eos_token

# Setup the templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root():
    return RedirectResponse(url="/generate-joke/")

@app.get("/generate-joke/", response_class=HTMLResponse)
async def get_joke_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/generate-joke/", response_class=HTMLResponse)
async def generate_joke(request: Request, prompt: str = Form(...)):
    inputs = tokenizer(prompt, return_tensors='pt', padding=True, truncation=True, max_length=512)
    input_ids = inputs['input_ids']
    attention_mask = inputs.get("attention_mask", None)

    outputs = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        num_return_sequences=1,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.9,
        top_k=50,
        top_p=0.9
    )

    generated_joke = tokenizer.decode(outputs[0], skip_special_tokens=True)
    joke = generated_joke.split('\n')[0]

    return templates.TemplateResponse("result.html", {"request": request, "prompt": prompt, "joke": joke})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8009)
