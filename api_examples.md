# API Examples

Here are some `curl` examples for interacting with the student management API.

## Get All Students

To get a list of all students, use the following command:

```bash
curl -X GET "http://127.0.0.1:8000/students"
```

## Add a New Student

To add a new student, use the following command. This example adds a student named "Bob" with a grade of 12.

```bash
curl -X POST "http://127.0.0.1:8002/students?name=Bob&grade=12"