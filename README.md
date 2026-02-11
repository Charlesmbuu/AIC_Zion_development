# 🏛 AIC Zambezi Digital Church Platform

A modern, scalable church management and evangelism platform built for **African Inland Church (AIC) – Zambezi, Kiambu, Kenya**.

Built with **Next.js, Supabase, and Vercel**, this platform enables sermon publishing, event management, and online giving in a clean, fast, and fully customizable system.

---

## 🚀 Live Demo

🔗 https://your-vercel-link.vercel.app  
*(Replace with your deployed URL)*

---

## 📌 Project Vision

To create a dynamic digital platform that:

- Supports church activities  
- Enhances community engagement  
- Enables online evangelism  
- Simplifies event and sermon management  
- Allows secure online donations  

This project is designed to scale from MVP to a fully-featured church ecosystem.

---

## 🛠 Tech Stack

### Frontend
- **Next.js (App Router)**
- **Tailwind CSS**
- Hosted on **Vercel**

### Backend
- **Supabase**
  - PostgreSQL Database
  - Authentication
  - Storage
  - Row-Level Security (RLS)

### Payments
- Flutterwave / Pesapal (redirect-based integration for MVP)

---

## 🏗 Core Features (MVP)

- 🏠 Homepage with dynamic content  
- 🎥 Sermon archive (YouTube embedded, DB-driven)  
- 📅 Events listing (dynamic from Supabase)  
- 💳 Online donation integration  
- 📍 Contact page with church details  
- 🔐 Admin authentication (Supabase Auth)  

---

## 🗄 Database Schema Overview

### Sermons

| Field        | Type      |
|-------------|----------|
| id          | UUID     |
| title       | Text     |
| preacher    | Text     |
| description | Text     |
| youtube_url | Text     |
| sermon_date | Date     |
| created_at  | Timestamp |

---

### Events

| Field        | Type      |
|-------------|----------|
| id          | UUID     |
| title       | Text     |
| description | Text     |
| event_date  | Date     |
| location    | Text     |
| image_url   | Text     |
| created_at  | Timestamp |

---

### Donations

| Field             | Type      |
|------------------|----------|
| id               | UUID     |
| name             | Text     |
| email            | Text     |
| amount           | Numeric  |
| payment_reference| Text     |
| created_at       | Timestamp |

---

git clone https://github.com/yourusername/aic-zambezi.git
cd aic-zambezi
