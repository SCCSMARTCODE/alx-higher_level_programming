#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: Pointer to the Python object.
 */
void print_python_bytes(PyObject *p) {
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size, i;
	unsigned char *raw;

	printf("[.] bytes object info\n");

	if (PyBytes_Check(p)) {
		size = PyBytes_GET_SIZE(p);
		raw = (unsigned char *)PyBytes_AS_STRING(p);

		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", raw);

		printf("  first %ld bytes: ", (size > 10) ? 10 : size);
		for (i = 0; i < size && i < 10; i++) {
			printf("%02x ", raw[i]);
		}
		printf("\n");
	} else {
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_list - Print information about a Python list.
 * @p: Pointer to the Python object.
 */
void print_python_list(PyObject *p) {
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, i;
	PyObject *element;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++) {
		element = list->ob_item[i];
		printf("Element %ld: ", i);
		if (PyBytes_Check(element)) {
			print_python_bytes(element);
		} else if (PyFloat_Check(element)) {
			printf("float\n");
		} else if (PyTuple_Check(element)) {
			printf("tuple\n");
		} else if (PyList_Check(element)) {
			printf("list\n");
		} else if (PyUnicode_Check(element)) {
			printf("str\n");
		} else if (PyLong_Check(element)) {
			printf("int\n");
		} else {
			printf("%s\n", Py_TYPE(element)->tp_name);
		}
	}
}

/**
 * main - Entry point for the program.
 * @argc: The number of command-line arguments.
 * @argv: An array of command-line argument strings.
 * Return: 0 upon successful execution.
 */
int main(int argc, char *argv[]) {
	Py_Initialize();
	// Define your Python objects and call the functions here.
	Py_Finalize();
	return 0;
}

