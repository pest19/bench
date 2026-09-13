# Pest Management CRM – Frappe

A Frappe Framework-based CRM and pest management workflow application developed for managing customers, quotations, work orders, and related business operations.

> **Development Branch:** `sharieff-development`

> **Repository:** https://github.com/pest19/bench/tree/sharieff-development

---

## 📌 Project Overview

This project extends the **Frappe Framework** to implement a customized Pest Management CRM workflow.

The system is designed to manage business processes such as:

* Customer management
* Quotations
* Quotation calculations
* Tax and discount handling
* Quotation approval workflow
* PDF quotation generation
* Emailing quotations
* Customer contact information
* Work Order creation
* WhatsApp integration/workflow
* Custom DocTypes and business logic

The project is developed using Frappe's **Bench development environment**.

---

## 🛠️ Technology Stack

* **Framework:** Frappe Framework
* **Backend:** Python
* **Frontend:** JavaScript / HTML / CSS
* **Database:** MariaDB
* **Cache & Background Jobs:** Redis
* **Package Management:** pip / Yarn
* **Development Environment:** Frappe Bench
* **Version Control:** Git / GitHub

---

# 🚀 Installation & Setup

## 1. Prerequisites

This project requires a Linux-based development environment.

If you are using Windows, it is recommended to use **Ubuntu through WSL**.

Required components include:

* Git
* Python
* Node.js
* Yarn
* MariaDB
* Redis
* Frappe Bench
* wkhtmltopdf

Frappe officially supports Linux distributions such as Ubuntu/Debian for manual installation. For Frappe v14/v15, the documented requirements include Python 3.10+, Node.js 18+, MariaDB 10.6.6+, Redis 6+, and Yarn 1.12+.

> **Note:** Use the versions compatible with the Frappe version used by this project.

---

# 📥 2. Clone the Repository

Clone the repository:

```bash
git clone https://github.com/pest19/bench.git
```

Enter the repository:

```bash
cd bench
```

Switch to the development branch containing my work:

```bash
git checkout sharieff-development
```

Verify the current branch:

```bash
git branch
```

You should see:

```text
* sharieff-development
```

---

# 🔧 3. Verify Bench Installation

Check whether Bench is installed:

```bash
bench --version
```

If Bench is not installed, follow the official Frappe installation documentation:

https://docs.frappe.io/framework/user/en/installation

Bench is the command-line tool used to manage Frappe applications and sites.

---

# 🗄️ 4. Create a Frappe Site

From the Bench directory, create a new site:

```bash
bench new-site pest.localhost
```

During this process, you will be asked for:

1. MariaDB root password
2. Administrator password

The Administrator password will be used to log in to the Frappe Desk.

Frappe creates a separate database for each site.

---

# 📦 5. Install the Project App

First, check the available applications:

```bash
ls apps
```

The custom Pest Management application should be present in the `apps` directory.

Install the application on the newly created site:

```bash
bench --site pest.localhost install-app pest_management
```


You can verify installed applications using:

```bash
bench --site pest.localhost list-apps
```

The output should include:

```text
frappe
<APP_NAME>
```

---

# ⚙️ 6. Enable Developer Mode

Enable developer mode:

```bash
bench set-config -g developer_mode 1
```

This is useful when working with custom DocTypes and other development features.

---

# 🔄 7. Run Database Migrations

Before starting the application, run:

```bash
bench --site pest.localhost migrate
```

This ensures that the site's database structure is synchronized with the application.

---

# ▶️ 8. Start the Frappe Server

Start the development server:

```bash
bench start
```

Keep this terminal running.

Frappe's development server normally runs on port `8000`.

---

# 🌐 9. Open the Application

Open the following URL in your browser:

```text
http://pest.localhost:8000
```

If the hostname does not resolve automatically, run:

```bash
bench --site pest.localhost add-to-hosts
```

Then open:

```text
http://pest.localhost:8000
```

Log in using:

```text
Username: Administrator
Password: <password-created-during-site-creation>
```

---

# 📋 Main Modules

## Customer Management

Customers can be created and managed along with their contact information and relevant business details.

---

## Quotation Management

The quotation module supports:

* Customer selection
* Customer contact number
* Service/product details
* Chemical cost
* Service cost
* Additional charges
* Discounts
* Tax calculations
* Grand total calculation
* Approval workflow
* Approval date
* Approved-by information
* Quotation print format
* PDF generation

---

## 📄 Quotation PDF

The quotation can be generated as a PDF using the configured Frappe Print Format.

The generated quotation can then be used for customer communication.

---

## 📧 Email Integration

The system supports sending quotations to customers through email.

The quotation PDF can be attached to the email.

---

## 📱 WhatsApp Workflow

The project also contains functionality related to sending quotation information through WhatsApp.

Some WhatsApp-related functionality may depend on external configuration/API information.

---

## 🛠️ Work Order

After the quotation/business process reaches the required stage, a Work Order can be created to continue the service workflow.

The Work Order is intended to carry the approved service information forward for operational processing.

---

# 📁 Project Structure

A typical Frappe Bench structure looks like:

```text
bench/
│
├── apps/
│   ├── frappe/
│   └── <custom-app>/
│
├── sites/
│   ├── apps.txt
│   ├── common_site_config.json
│   └── pest.localhost/
│
├── config/
├── env/
├── logs/
├── Procfile
└── README.md
```

The custom application is located inside:

```text
apps/<custom-app>/
```

Frappe Bench uses the `apps` directory for applications and the `sites` directory for individual Frappe sites.

---

# 🔍 Useful Commands

### Start the server

```bash
bench start
```

### Check installed applications

```bash
bench --site pest.localhost list-apps
```

### Run migrations

```bash
bench --site pest.localhost migrate
```

### Clear cache

```bash
bench --site pest.localhost clear-cache
```

### Build assets

```bash
bench build
```

### Open Frappe console

```bash
bench --site pest.localhost console
```

### Restart Bench

```bash
bench restart
```

### Check Bench status

```bash
bench doctor
```

---

# 🔄 Updating the Project

To get the latest changes from the repository:

```bash
git checkout sharieff-development
git pull origin sharieff-development
```

After pulling changes, run:

```bash
bench --site pest.localhost migrate
```

If frontend assets were changed:

```bash
bench build
```

Then restart the development server:

```bash
bench start
```

---

# ⚠️ Troubleshooting

### Site does not open

Make sure Bench is running:

```bash
bench start
```

Then check:

```text
http://pest.localhost:8000
```

---

### Application is not visible

Check installed applications:

```bash
bench --site pest.localhost list-apps
```

If the custom application is missing:

```bash
bench --site pest.localhost install-app <APP_NAME>
```

---

### Changes are not appearing

Run:

```bash
bench --site pest.localhost migrate
bench clear-cache
bench build
```

Then restart:

```bash
bench start
```

---

# 👨‍💻 Development Branch

All work covered in this documentation is available on:

```text
sharieff-development
```

Repository:

https://github.com/pest19/bench/tree/sharieff-development

The `sharieff-development` branch contains the development work implemented for the Pest Management CRM workflow.

---

# 📚 References

* Frappe Framework Documentation
  https://docs.frappe.io/framework/

* Frappe Installation Guide
  https://docs.frappe.io/framework/user/en/installation

* Frappe Bench Documentation
  https://docs.frappe.io/framework/user/en/bench

* GitHub Repository
  https://github.com/pest19/bench

---

## 👤 Developer

**Sharieff**

Development branch:

```text
sharieff-development
```
