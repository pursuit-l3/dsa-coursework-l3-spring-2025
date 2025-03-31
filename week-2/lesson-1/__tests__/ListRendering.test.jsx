import React from "react";
import { render, screen } from "@testing-library/react";
import TodoList from "../exercises/ListRendering";

describe("TodoList Component", () => {
  test("renders list items correctly", () => {
    const items = ["Learn React", "Build a project", "Deploy to production"];
    render(<TodoList items={items} />);

    expect(screen.getByText("Learn React")).toBeInTheDocument();
    expect(screen.getByText("Build a project")).toBeInTheDocument();
    expect(screen.getByText("Deploy to production")).toBeInTheDocument();

    const listItems = screen.getAllByRole("listitem");
    expect(listItems).toHaveLength(3);
  });

  test("renders empty state message when no items are provided", () => {
    render(<TodoList items={[]} />);
    expect(screen.getByText("No items to display")).toBeInTheDocument();
  });
});
