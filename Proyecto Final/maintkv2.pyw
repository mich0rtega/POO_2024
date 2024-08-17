import tkinter as tk
from tkinter import simpledialog, messagebox
from Medicos import medico
from Enfermeros import enfermero
from Paciente import paciente

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital 450")
        self.root.attributes('-fullscreen', True)  # Configura la ventana a pantalla completa

        self.user_medico = None
        self.user_enfermero = None

        self.current_frame = None
        self.menu_principal()

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    def menu_principal(self):
        self.clear_frame()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(fill='both', expand=True, padx=20, pady=20)

        tk.Label(self.current_frame, text="Hospital 450", font=("Arial", 24, "bold")).pack(pady=10)
        tk.Label(self.current_frame, text="Bienvenido al gestor de pacientes", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.current_frame, text="Registro Médico", command=self.registrar_medico, font=("Arial", 14)).pack(pady=10, fill='x')
        tk.Button(self.current_frame, text="Registro Enfermero", command=self.registrar_enfermero, font=("Arial", 14)).pack(pady=10, fill='x')
        tk.Button(self.current_frame, text="Login Médico", command=self.login_medico, font=("Arial", 14)).pack(pady=10, fill='x')
        tk.Button(self.current_frame, text="Login Enfermero", command=self.login_enfermero, font=("Arial", 14)).pack(pady=10, fill='x')
        tk.Button(self.current_frame, text="Salir", command=self.root.quit, font=("Arial", 14)).pack(pady=20, fill='x')

    def registrar_medico(self):
        self.clear_frame()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(fill='both', expand=True, padx=20, pady=20)

        tk.Label(self.current_frame, text="Registro de Médico", font=("Arial", 24, "bold")).pack(pady=20)

        def submit_registro_medico():
            nombre = nombre_var.get()
            apellidos = apellidos_var.get()
            numEmpleado = numEmpleado_var.get()
            password = password_var.get()
            especialidad = especialidad_var.get()
            turno = turno_var.get()

            obj_medico = medico.Medico(nombre, apellidos, numEmpleado, password, especialidad, turno)
            if obj_medico.registrar():
                messagebox.showinfo("Registro", "Médico registrado correctamente.")
                self.menu_principal()
            else:
                messagebox.showerror("Error", "No fue posible insertar el registro.")

        nombre_var = tk.StringVar()
        apellidos_var = tk.StringVar()
        numEmpleado_var = tk.StringVar()
        password_var = tk.StringVar()
        especialidad_var = tk.StringVar()
        turno_var = tk.StringVar()

        tk.Label(self.current_frame, text="Nombre:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=nombre_var, font=("Arial", 14)).pack(pady=5)

        tk.Label(self.current_frame, text="Apellidos:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=apellidos_var, font=("Arial", 14)).pack(pady=5)

        tk.Label(self.current_frame, text="Número de empleado:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=numEmpleado_var, font=("Arial", 14)).pack(pady=5)

        tk.Label(self.current_frame, text="Contraseña:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=password_var, show='*', font=("Arial", 14)).pack(pady=5)

        tk.Label(self.current_frame, text="Especialidad:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=especialidad_var, font=("Arial", 14)).pack(pady=5)

        tk.Label(self.current_frame, text="Turno:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=turno_var, font=("Arial", 14)).pack(pady=5)

        tk.Button(self.current_frame, text="Registrar", command=submit_registro_medico, font=("Arial", 14)).pack(pady=20)
        tk.Button(self.current_frame, text="Volver al Menú Principal", command=self.menu_principal, font=("Arial", 14)).pack()

    def registrar_enfermero(self):
        self.clear_frame()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(fill='both', expand=True, padx=20, pady=20)

        tk.Label(self.current_frame, text="Registro de Enfermero", font=("Arial", 24, "bold")).pack(pady=20)

        def submit_registro_enfermero():
            nombre = nombre_var.get()
            apellidos = apellidos_var.get()
            numEmpleado = numEmpleado_var.get()
            password = password_var.get()
            area = area_var.get()
            turno = turno_var.get()

            obj_enfermero = enfermero.Enfermero(nombre, apellidos, numEmpleado, password, area, turno)
            if obj_enfermero.registrar():
                messagebox.showinfo("Registro", "Enfermero registrado correctamente.")
                self.menu_principal()
            else:
                messagebox.showerror("Error", "No fue posible insertar el registro.")

        nombre_var = tk.StringVar()
        apellidos_var = tk.StringVar()
        numEmpleado_var = tk.StringVar()
        password_var = tk.StringVar()
        area_var = tk.StringVar()
        turno_var = tk.StringVar()

        tk.Label(self.current_frame, text="Nombre:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=nombre_var, font=("Arial", 14)).pack(pady=5)

        tk.Label(self.current_frame, text="Apellidos:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=apellidos_var, font=("Arial", 14)).pack(pady=5)

        tk.Label(self.current_frame, text="Número de empleado:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=numEmpleado_var, font=("Arial", 14)).pack(pady=5)

        tk.Label(self.current_frame, text="Contraseña:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=password_var, show='*', font=("Arial", 14)).pack(pady=5)

        tk.Label(self.current_frame, text="Área:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=area_var, font=("Arial", 14)).pack(pady=5)

        tk.Label(self.current_frame, text="Turno:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=turno_var, font=("Arial", 14)).pack(pady=5)

        tk.Button(self.current_frame, text="Registrar", command=submit_registro_enfermero, font=("Arial", 14)).pack(pady=20)
        tk.Button(self.current_frame, text="Volver al Menú Principal", command=self.menu_principal, font=("Arial", 14)).pack()

    def login_medico(self):
        self.clear_frame()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(fill='both', expand=True, padx=20, pady=20)

        tk.Label(self.current_frame, text="Login Médico", font=("Arial", 24, "bold")).pack(pady=20)

        def submit_login_medico():
            numEmpleado = numEmpleado_var.get()
            password = password_var.get()

            registro = medico.Medico.login(numEmpleado, password)
            if registro:
                self.user_medico = registro
                self.menu_medico()
            else:
                messagebox.showerror("Error", "Número de empleado o contraseña incorrectos.")

        numEmpleado_var = tk.StringVar()
        password_var = tk.StringVar()

        tk.Label(self.current_frame, text="Número de empleado:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=numEmpleado_var, font=("Arial", 14)).pack(pady=5)

        tk.Label(self.current_frame, text="Contraseña:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=password_var, show='*', font=("Arial", 14)).pack(pady=5)

        tk.Button(self.current_frame, text="Login", command=submit_login_medico, font=("Arial", 14)).pack(pady=20)
        tk.Button(self.current_frame, text="Volver al Menú Principal", command=self.menu_principal, font=("Arial", 14)).pack()

    def login_enfermero(self):
        self.clear_frame()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(fill='both', expand=True, padx=20, pady=20)

        tk.Label(self.current_frame, text="Login Enfermero", font=("Arial", 24, "bold")).pack(pady=20)

        def submit_login_enfermero():
            numEmpleado = numEmpleado_var.get()
            password = password_var.get()

            registro = enfermero.Enfermero.login(numEmpleado, password)
            if registro:
                self.user_enfermero = registro
                self.menu_enfermero()
            else:
                messagebox.showerror("Error", "Número de empleado o contraseña incorrectos.")

        numEmpleado_var = tk.StringVar()
        password_var = tk.StringVar()

        tk.Label(self.current_frame, text="Número de empleado:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=numEmpleado_var, font=("Arial", 14)).pack(pady=5)

        tk.Label(self.current_frame, text="Contraseña:", font=("Arial", 14)).pack()
        tk.Entry(self.current_frame, textvariable=password_var, show='*', font=("Arial", 14)).pack(pady=5)

        tk.Button(self.current_frame, text="Login", command=submit_login_enfermero, font=("Arial", 14)).pack(pady=20)
        tk.Button(self.current_frame, text="Volver al Menú Principal", command=self.menu_principal, font=("Arial", 14)).pack()

    def menu_medico(self):
        self.clear_frame()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(padx=20, pady=20)

        tk.Label(self.current_frame, text=f"Bienvenido(a) Dr. {self.user_medico[1]} {self.user_medico[2]}", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.current_frame, text="Registrar Paciente", command=self.registrar_paciente).pack(pady=5)
        tk.Button(self.current_frame, text="Registrar Diagnóstico y Receta", command=self.registrar_diagnostico_y_receta).pack(pady=5)
        tk.Button(self.current_frame, text="Ver Paciente", command=self.ver_paciente).pack(pady=5)
        tk.Button(self.current_frame, text="Cerrar Sesión", command=self.menu_principal).pack(pady=20)


    def menu_enfermero(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(padx=20, pady=20)

        tk.Label(self.current_frame, text=f"Bienvenido(a) Enfermero(a) {self.user_enfermero[1]} {self.user_enfermero[2]}", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.current_frame, text="Registrar Paciente", command=self.registrar_paciente).pack(pady=5)
        tk.Button(self.current_frame, text="Registrar Signos Vitales", command=self.registrar_signos_vitales).pack(pady=5)
        tk.Button(self.current_frame, text="Ver Paciente", command=self.ver_paciente).pack(pady=5)
        tk.Button(self.current_frame, text="Cerrar Sesión", command=self.menu_principal).pack(pady=20)

    def registrar_diagnostico_y_receta(self):
        self.clear_frame()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(padx=20, pady=20)

        tk.Label(self.current_frame, text="Registrar Diagnóstico y Receta", font=("Arial", 16)).pack(pady=20)

        def submit_registro_diagnostico_y_receta():
            id_paciente = id_paciente_var.get()
            diagnostico = diagnostico_var.get()
            receta = receta_var.get()

            obj_diagnostico = medico.Medico.registrar_diagnostico(id_paciente, diagnostico, receta)
            if obj_diagnostico:
                messagebox.showinfo("Registro", "Diagnóstico y receta registrados correctamente.")
                self.menu_medico()
            else:
                messagebox.showerror("Error", "No fue posible registrar el diagnóstico o la receta.")

        id_paciente_var = tk.StringVar()
        diagnostico_var = tk.StringVar()
        receta_var = tk.StringVar()

        tk.Label(self.current_frame, text="ID del paciente:").pack()
        tk.Entry(self.current_frame, textvariable=id_paciente_var).pack()

        tk.Label(self.current_frame, text="Diagnóstico:").pack()
        tk.Entry(self.current_frame, textvariable=diagnostico_var).pack()

        tk.Label(self.current_frame, text="Receta:").pack()
        tk.Entry(self.current_frame, textvariable=receta_var).pack()

        tk.Button(self.current_frame, text="Registrar", command=submit_registro_diagnostico_y_receta).pack(pady=20)
        tk.Button(self.current_frame, text="Volver al Menú Médico", command=self.menu_medico).pack()

    def registrar_signos_vitales(self):
        self.clear_frame()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(padx=20, pady=20)

        tk.Label(self.current_frame, text="Registrar Signos Vitales", font=("Arial", 16)).pack(pady=20)

        def submit_registro_signos_vitales():
            id_paciente = id_paciente_var.get()
            temperatura = temperatura_var.get()
            presion_sistolica = presion_sistolica_var.get()
            presion_diastolica = presion_diastolica_var.get()
            pulso = pulso_var.get()
            

            obj_signos = enfermero.Enfermero.registrar_signos_vitales(id_paciente, temperatura, presion_sistolica, presion_diastolica, pulso)
            if obj_signos:
                messagebox.showinfo("Registro", "Signos vitales registrados correctamente.")
                self.menu_enfermero()
            else:
                messagebox.showerror("Error", "No fue posible registrar los signos vitales.")

        id_paciente_var = tk.StringVar()
        temperatura_var = tk.StringVar()
        presion_sistolica_var = tk.StringVar()
        presion_diastolica_var = tk.StringVar()
        pulso_var = tk.StringVar()
       

        tk.Label(self.current_frame, text="ID del paciente:").pack()
        tk.Entry(self.current_frame, textvariable=id_paciente_var).pack()

        tk.Label(self.current_frame, text="Temperatura (°C):").pack()
        tk.Entry(self.current_frame, textvariable=temperatura_var).pack()

        tk.Label(self.current_frame, text="Presión Sistólica (mm Hg):").pack()
        tk.Entry(self.current_frame, textvariable=presion_sistolica_var).pack()

        tk.Label(self.current_frame, text="Presión Diastólica (mm Hg):").pack()
        tk.Entry(self.current_frame, textvariable=presion_diastolica_var).pack()

        tk.Label(self.current_frame, text="Pulso (bpm):").pack()
        tk.Entry(self.current_frame, textvariable=pulso_var).pack()

        tk.Button(self.current_frame, text="Registrar", command=submit_registro_signos_vitales).pack(pady=20)
        tk.Button(self.current_frame, text="Volver al Menú Enfermero", command=self.menu_enfermero).pack()

    def registrar_paciente(self):
        self.clear_frame()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(padx=20, pady=20)

        tk.Label(self.current_frame, text="Registrar Paciente", font=("Arial", 16)).pack(pady=20)

        def submit_registro_paciente():
            nombre = nombre_var.get()
            edad = edad_var.get()
            sexo = sexo_var.get()
            tipo_sangre = tipo_sangre_var.get()
            altura = altura_var.get()
            peso = peso_var.get()
            alergias = alergias_var.get()
            numero_cama = numero_cama_var.get()
            id_medico = id_medico_var.get()
            id_enfermero = id_enfermero_var.get()

            paciente_nuevo = paciente.Paciente(nombre, edad, sexo, tipo_sangre, altura, peso, alergias, numero_cama, id_medico, id_enfermero)
            if paciente_nuevo.registrar():
                messagebox.showinfo("Registro", "Paciente registrado correctamente.")
                if self.user_medico:
                    self.menu_medico()
                elif self.user_enfermero:
                    self.menu_enfermero()
            else:
                messagebox.showerror("Error", "Error al registrar el paciente.")

        nombre_var = tk.StringVar()
        edad_var = tk.StringVar()
        sexo_var = tk.StringVar()
        tipo_sangre_var = tk.StringVar()
        altura_var = tk.StringVar()
        peso_var = tk.StringVar()
        alergias_var = tk.StringVar()
        numero_cama_var = tk.StringVar()
        id_medico_var = tk.StringVar()
        id_enfermero_var = tk.StringVar()

        tk.Label(self.current_frame, text="Nombre:").pack()
        tk.Entry(self.current_frame, textvariable=nombre_var).pack()

        tk.Label(self.current_frame, text="Edad:").pack()
        tk.Entry(self.current_frame, textvariable=edad_var).pack()

        tk.Label(self.current_frame, text="Sexo:").pack()
        tk.Entry(self.current_frame, textvariable=sexo_var).pack()

        tk.Label(self.current_frame, text="Tipo de Sangre:").pack()
        tk.Entry(self.current_frame, textvariable=tipo_sangre_var).pack()

        tk.Label(self.current_frame, text="Altura (cm):").pack()
        tk.Entry(self.current_frame, textvariable=altura_var).pack()

        tk.Label(self.current_frame, text="Peso (kg):").pack()
        tk.Entry(self.current_frame, textvariable=peso_var).pack()

        tk.Label(self.current_frame, text="Alergias:").pack()
        tk.Entry(self.current_frame, textvariable=alergias_var).pack()

        tk.Label(self.current_frame, text="Número de Cama:").pack()
        tk.Entry(self.current_frame, textvariable=numero_cama_var).pack()

        tk.Label(self.current_frame, text="ID Médico que atendió:").pack()
        tk.Entry(self.current_frame, textvariable=id_medico_var).pack()

        tk.Label(self.current_frame, text="ID Enfermero que atendió:").pack()
        tk.Entry(self.current_frame, textvariable=id_enfermero_var).pack()

        tk.Button(self.current_frame, text="Registrar", command=submit_registro_paciente).pack(pady=20)
        tk.Button(self.current_frame, text="Volver al Menú Médico" if self.user_medico else "Volver al Menú Enfermero", command=self.menu_medico if self.user_medico else self.menu_enfermero).pack()

    def ver_paciente(self):
        self.clear_frame()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(padx=20, pady=20)

        tk.Label(self.current_frame, text="Ver Paciente", font=("Arial", 16)).pack(pady=20)

        id_paciente = simpledialog.askstring("Input", "ID del paciente:", parent=self.root)
        paciente_info = paciente.Paciente.obtener(id_paciente)
        signos_vitales = enfermero.Enfermero.obtenerSignos(id_paciente)

        if paciente_info:
            tk.Label(self.current_frame, text="Información del Paciente").pack(pady=10)
            tk.Label(self.current_frame, text=f"Nombre: {paciente_info[1]}").pack()
            tk.Label(self.current_frame, text=f"Edad: {paciente_info[2]}").pack()
            tk.Label(self.current_frame, text=f"Sexo: {paciente_info[3]}").pack()
            tk.Label(self.current_frame, text=f"Tipo de Sangre: {paciente_info[4]}").pack()
            tk.Label(self.current_frame, text=f"Altura: {paciente_info[5]} cm").pack()
            tk.Label(self.current_frame, text=f"Peso: {paciente_info[6]} kg").pack()
            tk.Label(self.current_frame, text=f"Alergias: {paciente_info[7]}").pack()
            tk.Label(self.current_frame, text=f"Número de Cama: {paciente_info[8]}").pack()

            if signos_vitales:
                tk.Label(self.current_frame, text="Signos Vitales").pack(pady=10)
                for signo in signos_vitales:
                    tk.Label(self.current_frame, text=f"Temperatura: {signo[2]} °C").pack()
                    tk.Label(self.current_frame, text=f"Presión Sistólica: {signo[3]} mm Hg").pack()
                    tk.Label(self.current_frame, text=f"Presión Diastólica: {signo[4]} mm Hg").pack()
                    tk.Label(self.current_frame, text=f"Pulso: {signo[5]} bpm").pack()
                    tk.Label(self.current_frame, text=f"Estado: {signo[6]}").pack()
                    tk.Label(self.current_frame, text=f"Fecha: {signo[7]}").pack()
            else:
                tk.Label(self.current_frame, text="No se encontraron signos vitales para este paciente.").pack()

        else:
            tk.Label(self.current_frame, text="No se encontró información para este paciente.").pack()

        tk.Button(self.current_frame, text="Volver", command=self.menu_medico if self.user_medico else self.menu_enfermero).pack(pady=20)



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
