import React from "react";
import { render, screen } from "@testing-library/react";
import UserStatus from "../exercises/ConditionalRendering";

describe("UserStatus Component", () => {
  test("renders welcome message when user is logged in", () => {
    render(<UserStatus isLoggedIn={true} username="Alice" />);
    expect(screen.getByText("Welcome back, Alice!")).toBeInTheDocument();
  });

  test("renders login prompt when user is not logged in", () => {
    render(<UserStatus isLoggedIn={false} username="Alice" />);
    expect(screen.getByText("Please log in")).toBeInTheDocument();
  });
});
