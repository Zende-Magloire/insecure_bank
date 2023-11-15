This banking website allows users to withdraw money from their account. The code is deliberately left vulnerable to demonstrate the importance of sanitizing user input.

The / route of this application enables a user to input an amount of money to withdraw without undergoing any input validation or sanitization.

The exception thrown when the withdrawal fails is impractical as it doesn't display an error message. Instead, it fails silently, reflecting the value in the URL. This reflection in the URL indicates that the entered string is being sent back in the response without proper sanitization or escaping.

For instance, entering a script like <script>alert(1)</script> is reflected in the URL but doesn't execute immediately. However, this doesn't necessarily mean the application isn't vulnerable; it might suggest that the attack payload isn't currently executed or that additional contexts are needed for successful exploitation.

If the application's context allowed for JavaScript execution, such as in a different part of the application where the input is reflected directly into an HTML page, an attacker could craft a URL containing malicious scripts that execute when visited by another user. This could lead to cross-site scripting (XSS) attacks, allowing attackers to steal cookies or perform actions on behalf of another user.

This behavior encourages further experimentation with other inputs to observe results, such as negative numbers or amounts that exceed the user's current balance. A negative number input successfully alters the remaining balance. Conversely, entering a number exceeding the user's balance is also successful, leaving the remaining balance unchanged.
