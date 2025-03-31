import React from "react";
import { render, screen } from "@testing-library/react";
import UserProfile from "../exercises/PropsDestructuring";

describe("UserProfile Component", () => {
  test("renders user information correctly", () => {
    render(
      <UserProfile
        name="John Doe"
        age={30}
        email="john@example.com"
        location="New York"
      />
    );

    expect(screen.getByText("John Doe")).toBeInTheDocument();
    expect(screen.getByText("Age: 30")).toBeInTheDocument();
    expect(screen.getByText("Email: john@example.com")).toBeInTheDocument();
    expect(screen.getByText("Location: New York")).toBeInTheDocument();
  });
});
