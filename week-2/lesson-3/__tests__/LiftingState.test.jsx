import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import Parent from "../exercises/LiftingState";

describe("Lifting State Up", () => {
  test("renders with initial theme", () => {
    render(<Parent />);
    expect(screen.getByText(/Current theme: light/)).toBeInTheDocument();
  });

  test("toggles theme when button is clicked", () => {
    render(<Parent />);

    // Initial state
    expect(screen.getByText(/Current theme: light/)).toBeInTheDocument();

    // Click toggle button
    fireEvent.click(screen.getByText("Toggle Theme"));

    // Theme should change
    expect(screen.getByText(/Current theme: dark/)).toBeInTheDocument();

    // Click toggle button again
    fireEvent.click(screen.getByText("Toggle Theme"));

    // Theme should change back
    expect(screen.getByText(/Current theme: light/)).toBeInTheDocument();
  });
});
