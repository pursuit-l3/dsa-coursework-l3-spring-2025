import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import Counter from "../exercises/CounterState";

describe("Counter Component", () => {
  test("renders with initial count of 0", () => {
    render(<Counter />);
    expect(screen.getByText(/0/)).toBeInTheDocument();
  });

  test("increments count when Increment button is clicked", () => {
    render(<Counter />);
    fireEvent.click(screen.getByText("Increment"));
    expect(screen.getByText(/1/)).toBeInTheDocument();
  });

  test("decrements count when Decrement button is clicked", () => {
    render(<Counter />);
    fireEvent.click(screen.getByText("Increment"));
    fireEvent.click(screen.getByText("Increment"));
    fireEvent.click(screen.getByText("Decrement"));
    expect(screen.getByText(/1/)).toBeInTheDocument();
  });

  test("resets count when Reset button is clicked", () => {
    render(<Counter />);
    fireEvent.click(screen.getByText("Increment"));
    fireEvent.click(screen.getByText("Increment"));
    fireEvent.click(screen.getByText("Reset"));
    expect(screen.getByText(/0/)).toBeInTheDocument();
  });
});
