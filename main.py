import requests

def generate_webhook():
    url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

    payload = {
        "name": "Sakshi Ishwe",
        "regNo": "REG12347",
        "email": "sakshi.svvv.ishwe@gmail.com"
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        print("✅ Webhook Generated Successfully")
        return data
    else:
        print("❌ Error:", response.status_code)
        print("Message:", response.text)
        return None

def submit_final_query(webhook_url, access_token):
    # Replace this with your actual SQL solution
    final_sql_query = """
     SELECT
    ->     P.AMOUNT AS SALARY,
    ->     CONCAT(E.FIRST_NAME, ' ', E.LAST_NAME) AS NAME,
    ->     FLOOR(DATEDIFF('2025-05-11', E.DOB) / 365.25) AS AGE,
    ->     D.DEPARTMENT_NAME
    -> FROM PAYMENTS P
    -> JOIN EMPLOYEE E ON P.EMP_ID = E.EMP_ID
    -> JOIN DEPARTMENT D ON E.DEPARTMENT = D.DEPARTMENT_ID
    -> WHERE P.AMOUNT = (
    ->     SELECT MAX(AMOUNT)
    ->     FROM PAYMENTS
    ->     WHERE EXTRACT(DAY FROM PAYMENT_TIME) != 1
    -> );
    """

    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }

    body = {
        "finalQuery": final_sql_query.strip()
    }

    response = requests.post(webhook_url, headers=headers, json=body)

    if response.status_code == 200:
        print("✅ Final SQL query submitted successfully!")
    else:
        print("❌ Submission Failed:", response.status_code)
        print("Message:", response.text)

if __name__ == "__main__":
    data = generate_webhook()
    if data:
        submit_final_query(data["webhook"], data["accessToken"])
