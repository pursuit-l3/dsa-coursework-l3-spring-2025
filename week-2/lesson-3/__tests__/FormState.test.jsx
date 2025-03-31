import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import LoginForm from "../exercises/FormState";

describe("LoginForm Component", () => {
  test("updates username state when input changes", () => {
    render(<LoginForm />);
    const usernameInput =
      screen.getByPlaceholderText("Username") ||
      screen.getByLabelText("Username");

    fireEvent.change(usernameInput, { target: { value: "testuser" } });

    expect(usernameInput.value).toBe("testuser");
  });

  test("updates password state when input changes", () => {
    render(<LoginForm />);
    const passwordInput =
      screen.getByPlaceholderText("Password") ||
      screen.getByLabelText("Password");

    fireEvent.change(passwordInput, { target: { value: "password123" } });

    expect(passwordInput.value).toBe("password123");
  });

  test("updates rememberMe state when checkbox is clicked", () => {
    render(<LoginForm />);
    const checkbox =
      screen.getByLabelText("Remember me") || screen.getByRole("checkbox");

    expect(checkbox.checked).toBe(false);
    fireEvent.click(checkbox);
    expect(checkbox.checked).toBe(true);
  });

  test("calls handleSubmit when form is submitted", () => {
    const consoleSpy = jest.spyOn(console, "log").mockImplementation();

    render(<LoginForm />);
    const usernameInput =
      screen.getByPlaceholderText("Username") ||
      screen.getByLabelText("Username");
    const passwordInput =
      screen.getByPlaceholderText("Password") ||
      screen.getByLabelText("Password");
    const submitButton = screen.getByRole("button", { name: /submit/i });

    fireEvent.change(usernameInput, { target: { value: "testuser" } });
    fireEvent.change(passwordInput, { target: { value: "password123" } });
    fireEvent.click(submitButton);

    expect(consoleSpy).toHaveBeenCalled();

    consoleSpy.mockRestore();
  });
});
