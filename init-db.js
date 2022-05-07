db = db.getSiblingDB("customer_db");
db.customer_tb.drop();

db.customer_tb.insertMany([
    {
        "name": "Nome 1",
        "birth_data": "1651927340",
        "address": [
            {
                "cep": "000100-000",
                "number_address": "8000",
                "type": "COMERCIAL"
            },
            {
                "cep": "000101-000",
                "number_address": "8000",
                "type": "COMERCIAL"
            }
        ],
        "email": [
            {
                "email": "email@teste.com.br"
            },
            {
                "email": "email2@teste.com.br"
            }
        ]
    },
    {
        "name": "Nome 3",
        "birth_data": "1651927355",
        "address": [
            {
                "cep": "000100-000",
                "number_address": "8700",
                "type": "COMERCIAL"
            },
            {
                "cep": "000101-000",
                "number_address": "80430",
                "type": "COMERCIAL"
            }
        ],
        "email": [
            {
                "email": "emailjdda@teste.com.br"
            },
            {
                "email": "email2fds@teste.com.br"
            }
        ]
    },
    {
        "name": "Nome 3",
        "birth_data": "1651927399",
        "address": [
            {
                "cep": "000100-000",
                "number_address": "8870",
                "type": "COMERCIAL"
            },
            {
                "cep": "000101-000",
                "number_address": "80210",
                "type": "COMERCIAL"
            }
        ],
        "email": [
            {
                "email": "emailqwe@teste.com.br"
            },
            {
                "email": "email2rew@teste.com.br"
            }
        ]
    },
]);