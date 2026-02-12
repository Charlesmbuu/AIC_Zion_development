import { ReactNode } from "react";

export default function Section({ children }: { children: ReactNode }) {
  return (
    <section className="py-20 px-6 max-w-7xl mx-auto">
      {children}
    </section>
  );
}
