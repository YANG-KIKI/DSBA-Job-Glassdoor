# submit_test_entry.py

from firebase_utils import init_firebase
import firebase_admin.db as db

# 初始化 Firebase 连接
init_firebase()

# 模拟用户邮箱（用于数据结构中的路径）
test_email = "kiki.test@example.com"
path = test_email.replace(".", "_")

# 模拟数据内容
test_entry = {
    "name": "Kiki (Test)",
    "nationality": "China",
    "company": "OpenAI",
    "role": "ML Intern",
    "application_method": "LinkedIn",
    "city": "Paris",
    "language": "English",
    "rounds": {
        "1": {
            "questions": "Tell me about a project where you used ML.",
            "advice": "Prepare examples with clear metrics.",
            "result": "Passed"
        }
    }
}

# 上传数据到 Firebase
ref = db.reference("/")
ref.child(path).set(test_entry)

print("✅ Test entry submitted to Firebase.")
