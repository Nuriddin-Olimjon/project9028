cost_types = [
    {
        # 1
        "title": "Communal payments"
    },
    {
        # 2
        "title": "Food payments"
    }
]

expenses = [
    {
        "cost_type_id": 1,
        "invoice_id": None,
        "returned_invoice_id": None,
        "amount": 1000,
        "description": "Monthly payment for all communal payments"
    },
    {
        "cost_type_id": 2,
        "invoice_id": None,
        "returned_invoice_id": None,
        "amount": 200,
        "description": "For lunch"
    },
    {
        "cost_type_id": 2,
        "invoice_id": None,
        "returned_invoice_id": None,
        "amount": 300,
        "description": "For lunch"
    },
    {
        "cost_type_id": None,
        "invoice_id": 1,
        "returned_invoice_id": None,
        "amount": 0, # TODO: calculate from invoice
        "description": "Full payment for invoice 1"
    },
    {
        "cost_type_id": None,
        "invoice_id": 2,
        "returned_invoice_id": None,
        "amount": 0, # TODO: calculate from invoice
        "description": "Half payment for invoice 2"
    },
    {
        "cost_type_id": None,
        "invoice_id": None,
        "returned_invoice_id": 1,
        "amount": 0, # TODO: calculate from returned invoice
        "description": "Full payment for invoice 1"
    },
]
