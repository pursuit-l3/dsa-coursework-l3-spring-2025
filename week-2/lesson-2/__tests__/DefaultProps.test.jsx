import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import Button from "../exercises/DefaultProps";

describe("Button Component", () => {
  test("renders with custom props", () => {
    const handleClick = jest.fn();
    render(
      <Button
        text="Submit"
        color="success"
        size="large"
        onClick={handleClick}
      />
    );

    const button = screen.getByText("Submit");
    expect(button).toBeInTheDocument();
    expect(button).toHaveClass("btn btn-success btn-large");

    fireEvent.click(button);
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  test("renders with default props", () => {
    render(<Button onClick={() => {}} />);

    const button = screen.getByText("Click me");
    expect(button).toBeInTheDocument();
    expect(button).toHaveClass("btn btn-primary btn-medium");
  });
});
