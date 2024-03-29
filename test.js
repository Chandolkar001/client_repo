// vulnerable_code.js
// 
// Example 1: Command Injection
const exec = require('child_process').exec;
const userInput = process.argv[2];
exec('echo ' + userInput);

// Example 2: SQL Injection
const userId = process.argv[3];
const query = 'SELECT * FROM users WHERE id = ' + userId;
// Assume this query is executed on a database

// Example 3: XSS (Cross-Site Scripting)
const userInputXSS = process.argv[4];
document.write('<p>' + userInputXSS + '</p>');

// Example 4: Insecure Password Handling
const userPassword = process.argv[5];
// Assume this password is stored in plaintext

// Example 5: Use of weak cryptographic function
const crypto = require('crypto');
const weakHash = (password) => crypto.createHash('md5').update(password).digest('hex');
const userPasswordHashed = process.argv[6];
console.log('Hashed Password:', weakHash(userPasswordHashed));
