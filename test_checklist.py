"""
Verification script testing all 10 checklist items specified in the assignment.
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def run_tests():
    print("========================================")
    print("Running Student CRUD API Checklist Tests")
    print("========================================")

    # Test 1: Create a valid student (201 Created)
    payload_valid = {
        "name": "Karan Mehra",
        "email": "karan.m@example.com",
        "course": "B.Tech Computer Science",
        "semester": 1
    }
    res1 = client.post("/students", json=payload_valid)
    assert res1.status_code == 201, f"Test 1 Failed: Expected 201, got {res1.status_code}"
    new_student = res1.json()
    new_id = new_student["id"]
    assert new_student["name"] == payload_valid["name"]
    print(f"PASS [Test 1] Create valid student -> Status {res1.status_code}, ID: {new_id}")

    # Test 2: Create a student with invalid data (422 Unprocessable Entity)
    payload_invalid = {
        "name": "",  # invalid: min_length=1
        "email": "invalid",
        "course": "B.Tech",
        "semester": 15  # invalid: le=12
    }
    res2 = client.post("/students", json=payload_invalid)
    assert res2.status_code == 422, f"Test 2 Failed: Expected 422, got {res2.status_code}"
    print(f"PASS [Test 2] Create invalid student -> Status {res2.status_code} (Validation error)")

    # Test 3: Get all students (200 OK + list)
    res3 = client.get("/students")
    assert res3.status_code == 200, f"Test 3 Failed: Expected 200, got {res3.status_code}"
    students_list = res3.json()
    assert isinstance(students_list, list) and len(students_list) >= 5
    print(f"PASS [Test 3] Get all students -> Status {res3.status_code}, Count: {len(students_list)}")

    # Test 4: Get an existing student ID (200 OK + student)
    res4 = client.get(f"/students/{new_id}")
    assert res4.status_code == 200, f"Test 4 Failed: Expected 200, got {res4.status_code}"
    assert res4.json()["id"] == new_id
    print(f"PASS [Test 4] Get existing student ID {new_id} -> Status {res4.status_code}")

    # Test 5: Get a non-existing student ID (404 Not Found)
    res5 = client.get("/students/99999")
    assert res5.status_code == 404, f"Test 5 Failed: Expected 404, got {res5.status_code}"
    print(f"PASS [Test 5] Get non-existing student ID 99999 -> Status {res5.status_code}")

    # Test 6: Update an existing student (200 OK + updated student)
    payload_update = {
        "name": "Karan Mehra Updated",
        "email": "karan.updated@example.com",
        "course": "B.Tech AI & Data Science",
        "semester": 2
    }
    res6 = client.put(f"/students/{new_id}", json=payload_update)
    assert res6.status_code == 200, f"Test 6 Failed: Expected 200, got {res6.status_code}"
    assert res6.json()["name"] == "Karan Mehra Updated"
    print(f"PASS [Test 6] Update existing student ID {new_id} -> Status {res6.status_code}")

    # Test 7: Update a non-existing student ID (404 Not Found)
    res7 = client.put("/students/99999", json=payload_update)
    assert res7.status_code == 404, f"Test 7 Failed: Expected 404, got {res7.status_code}"
    print(f"PASS [Test 7] Update non-existing student ID 99999 -> Status {res7.status_code}")

    # Test 8: Delete an existing student (204 No Content)
    res8 = client.delete(f"/students/{new_id}")
    assert res8.status_code == 204, f"Test 8 Failed: Expected 204, got {res8.status_code}"
    print(f"PASS [Test 8] Delete existing student ID {new_id} -> Status {res8.status_code}")

    # Test 9: Delete a non-existing student ID (404 Not Found)
    res9 = client.delete("/students/99999")
    assert res9.status_code == 404, f"Test 9 Failed: Expected 404, got {res9.status_code}"
    print(f"PASS [Test 9] Delete non-existing student ID 99999 -> Status {res9.status_code}")

    # Test 10: Verify deleted student cannot be retrieved (404 Not Found)
    res10 = client.get(f"/students/{new_id}")
    assert res10.status_code == 404, f"Test 10 Failed: Expected 404, got {res10.status_code}"
    print(f"PASS [Test 10] Verify deleted student cannot be retrieved -> Status {res10.status_code}")

    print("========================================")
    print("All 10 Checklist Tests Passed Successfully!")
    print("========================================")

if __name__ == "__main__":
    run_tests()
