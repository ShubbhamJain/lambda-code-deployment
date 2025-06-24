FROM public.ecr.aws/lambda/python:3.11

COPY app.py ./

# 3. (Optional) Install dependencies
COPY requirements.txt ./
#RUN pip install -r requirements.txt

CMD ["app.lambda_handler"]