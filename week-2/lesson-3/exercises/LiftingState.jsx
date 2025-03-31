// Exercise: Implement lifting state up
// 1. Create a component called 'Parent' that:
//    - Uses useState to track a 'theme' state (either "light" or "dark")
//    - Renders the current theme and two child components: ThemeDisplay and ThemeToggle
// 2. Create a component called 'ThemeDisplay' that:
//    - Accepts props: theme
//    - Renders a div with text "Current theme: {theme}"
// 3. Create a component called 'ThemeToggle' that:
//    - Accepts props: onToggle
//    - Renders a button with text "Toggle Theme" that calls onToggle when clicked
// 4. Export the Parent component as the default export

import React, { useState } from "react";

// Write your code here:
