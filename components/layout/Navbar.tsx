"use client";

import Link from "next/link";

export default function Navbar() {
  return (
    <header className="sticky top-0 z-50 bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        <h1 className="font-bold text-xl text-[#C8102E]">
          AIC Zambezi
        </h1>

        <nav className="hidden md:flex gap-6 text-sm font-medium">
          <Link href="/">Home</Link>
          <Link href="/sermons">Sermons</Link>
          <Link href="/events">Events</Link>
          <Link href="/ministries">Ministries</Link>
          <Link href="/give">Give</Link>
          <Link href="/contact">Contact</Link>
        </nav>
      </div>
    </header>
  );
}
