import Hero from "@/components/sections/Hero";
import ServiceTimes from "@/components/sections/ServiceTimes";
import SermonPreview from "@/components/sections/SermonPreview";
import EventPreview from "@/components/sections/EventPreview";
import CallToAction from "@/components/sections/CallToAction";

export default function HomePage() {
  return (
    <>
      <Hero />
      <ServiceTimes />
      <SermonPreview />
      <EventPreview />
      <CallToAction />
    </>
  );
}
