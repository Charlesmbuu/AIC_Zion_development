import Section from "../ui/Section";
import Button from "../ui/Button";

export default function Hero() {
  return (
    <Section>
      <div className="text-center space-y-6">
        <h1 className="text-4xl md:text-6xl font-bold">
          Building Faith. Serving Community.
        </h1>
        <p className="text-lg text-neutral-600">
          Welcome to African Inland Church Zambezi
        </p>
        <Button>Join Us This Sunday</Button>
      </div>
    </Section>
  );
}
