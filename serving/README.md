https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset

# Server with FastAPI
### To cover
- [ ] displaying the API documentation
- [ ] parameter validation (required, optional, etc)

#### Data validation
- With Pydantic
    - https://pydantic-docs.helpmanual.io/
    - https://pydantic-docs.helpmanual.io/usage/types/#strict-types

### Links
- [Getting started with FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/)
- https://fastapi.tiangolo.com/tutorial/bigger-applications/

### Doc
1. Create a file `main.py` where you define your app

2. Launch the server
    - From the terminal with `uvicorn`
    ```shell
    $ uvicorn main:app --reload
    ```
   - Or with Python
   ```python
   import uvicorn
   
   if __name__ == '__main__':
       uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)
   ```
   
   ```shell
   $ python main.py
   ```
- Here
    - `uvicorn`: server (for more information https://www.uvicorn.org/)
    - `main`: the Python module where the API is defined (app = FastAPI())
    - `app`: the object created inside of `main.py` with the line app = FastAPI().
    - `--reload`: make the server restart after code changes. Only use for development.

3. Do a request to the API
   - By typing the address in your browser (http://127.0.0.1:8000)
   - Or doing a request from your terminal
   ```shell
   $ curl -X GET http://127.0.0.1:8000
   ```

4. Display the documentation of your API by visiting `http://localhost:8000/docs`
   
n. Make a prediction by
   - Typing this url in  your browser `http://0.0.0.0:8000/predict?age=59&sex=2&bmi=32.1&bp=101&s1=157&s2=93.2&s3=38&s4=4&s5=4.8598&s6=87&s7=151`
   - Or by executing this command in your terminal
   ```shell
   $ curl -X 'POST' \
       'http://localhost:8000/predict' \
       -H 'accept: application/json' \
       -H 'Content-Type: application/json' \
       -d '{
          "age": 0, "sex": 0, "bmi": 0, "bp": 0, "s1": 0, "s2": 0, "s3": 0, "s4": 0, "s5": 0, "s6": 0
       }'
   ```

# Streamlit
https://docs.streamlit.io/en/stable/




