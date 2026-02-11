This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.

# 🏛 AIC Zambezi Digital Church Platform

A modern, scalable church management and evangelism platform built for **African Inland Church (AIC) – Zambezi, Kiambu, Kenya**.

Built with **Next.js, Supabase, and Vercel**, this platform enables sermon publishing, event management, and online giving in a clean, fast, and fully customizable system.

---

## 🚀 Live Demo

🔗 https://your-vercel-link.vercel.app  
*(TO Replace with deployed URL once complete!)*

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


## 🎨 Design System

### Theme Colors (AIC Inspired)

  - Red: #C8102E
  
  - Gold: #FFD700
  
  - White: #FFFFFF
  
  - Dark Accent: #111111


---

## 🔒 Security

- Supabase Row-Level Security enabled

- Environment variables secured

- HTTPS via Vercel

- Auth-protected admin routes

---

## 📈 Future Roadmap

- Member authentication dashboard

- Prayer request system

- Newsletter integration

- SMS notifications

- Advanced donation analytics

- Media upload system (beyond YouTube embeds)

---

## 🤝 Contributors

- Charles Mburu – Project Lead / Frontend

- Kelvin Thairu – Backend / Systems

---

## 📜 License
MIT License

---
