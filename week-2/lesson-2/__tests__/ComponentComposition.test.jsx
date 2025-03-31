import React from "react";
import { render, screen } from "@testing-library/react";
import ProfileCard from "../exercises/ComponentComposition";

describe("Component Composition", () => {
  test("ProfileCard renders correctly with Card component", () => {
    render(
      <ProfileCard
        name="Jane Smith"
        bio="Software developer with 5 years of experience"
      />
    );

    expect(screen.getByText("Jane Smith")).toBeInTheDocument();
    expect(
      screen.getByText("Software developer with 5 years of experience")
    ).toBeInTheDocument();

    // Check that the card structure exists
    const cardHeader = document.querySelector(".card-header");
    const cardBody = document.querySelector(".card-body");

    expect(cardHeader).toBeInTheDocument();
    expect(cardBody).toBeInTheDocument();
  });
});
