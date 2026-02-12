import { ReactNode } from "react";

interface Props {
  children: ReactNode;
  variant?: "primary" | "gold";
}

export default function Button({ children, variant = "primary" }: Props) {
  const styles =
    variant === "primary"
      ? "bg-[#C8102E] text-white"
      : "bg-[#FFD700] text-black";

  return (
    <button
      className={`px-6 py-3 rounded-xl font-semibold transition hover:opacity-90 ${styles}`}
    >
      {children}
    </button>
  );
}
