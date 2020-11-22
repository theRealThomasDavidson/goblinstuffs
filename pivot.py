    float rotationSpeed = 45;
    Vector3 currentEulerAngles;
    Quaternion currentRotation;
    float x;
    float y;
    float z;

    void Update()
        {
            if (Input.GetKeyDown(KeyCode.Q)) y = 1 - y;
            if (Input.GetKeyDown(KeyCode.E)) y = 1 + y;

            //modifying the Vector3, based on input multiplied by speed and time
            currentEulerAngles += new Vector3(x, y, z) * Time.deltaTime * rotationSpeed;

            //moving the value of the Vector3 into Quanternion.eulerAngle format
            currentRotation.eulerAngles = currentEulerAngles;

            //apply the Quaternion.eulerAngles change to the gameObject
            GetComponent<Rigidbody>().rotation = currentRotation;
        }
