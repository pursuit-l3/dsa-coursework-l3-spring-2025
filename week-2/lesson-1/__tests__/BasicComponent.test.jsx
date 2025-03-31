import React from "react";
import { render, screen } from "@testing-library/react";
import Greeting from "../exercises/BasicComponent";

describe("Greeting Component", () => {
  test("renders with provided name", () => {
    render(<Greeting name="Alice" />);
    expect(screen.getByText("Hello, Alice!")).toBeInTheDocument();
  });

  test("renders with default name when no name is provided", () => {
    render(<Greeting />);
    expect(screen.getByText("Hello, World!")).toBeInTheDocument();
  });
});
