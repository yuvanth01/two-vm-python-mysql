# Two VM Python MySQL Project

## 📌 Project Overview
This project demonstrates a client–server architecture using two Ubuntu virtual machines connected via a network.

- **VM 1 (Server):** Runs MySQL server and Python code to create the database
- **VM 2 (Client):** Runs Python client code to connect and query the database remotely

---

## 🛠️ Technologies Used
- Python 3
- MySQL
- Ubuntu (VMware Workstation)
- Virtual Environments (venv)
- Git & GitHub

---

## 🧩 Project Structure

---

## ⚙️ How It Works
1. MySQL server is installed on **VM 1**
2. Database and tables are created using Python
3. A MySQL user (`clientuser`) is created for remote access
4. Client VM connects using environment variables
5. Queries are executed from VM 2 and results are returned


---

##  SAVE & EXIT

- Press **CTRL + O**
- Press **Enter**
- Press **CTRL + X**

---

##  COMMIT README TO GITHUB

```bash
git add README.md
git commit -m "Add README with project explanation"
git push
---

## 🔐 Environment Variables (Client VM)
```bash
export DB_HOST=<SERVER_IP>
export DB_CLIENT_USER=clientuser
export DB_CLIENT_PASSWORD=client123
