import tkinter as tk
from tkinter import messagebox
from Medicos import medico
from Enfermeros import enfermero
from Paciente import paciente

def on_enter(event):
    event.widget.config(bg="black", fg="white")

def on_leave(event):
    event.widget.config(bg="white", fg="black")

def menu_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Hospital 450")
    ventana_principal.geometry("500x400")

    def registrar_medico():
        ventana_registro = tk.Toplevel(ventana_principal)
        ventana_registro.title("Registro de Médico")
        ventana_registro.geometry("400x400")

        labels = ["Nombre:", "Apellidos:", "Email:", "Contraseña:", "Especialidad:", "Turno:"]
        entries = []

        for i, label_text in enumerate(labels):
            label = tk.Label(ventana_registro, text=label_text, font=("Arial", 12), bg="white", fg="black")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(ventana_registro, font=("Arial", 12), bg="white", fg="black", width=30, show="*" if "Contraseña" in label_text else None)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry.bind("<Enter>", on_enter)
            entry.bind("<Leave>", on_leave)
            entries.append(entry)

        def registrar():
            nombre = entry_nombre.get()
            apellidos = entry_apellidos.get()
            email = entry_email.get()
            password = entry_password.get()
            especialidad = entry_especialidad.get()
            turno = entry_turno.get()
            obj_medico = medico.Medico(nombre, apellidos, email, password, especialidad, turno)
            if obj_medico.registrar():
                messagebox.showinfo("Éxito", f"{nombre} {apellidos}, se registró correctamente, con el email {email}")
            else:
                messagebox.showerror("Error", "No fue posible registrar el médico. Inténtelo de nuevo más tarde.")
            ventana_registro.destroy()

        entry_nombre, entry_apellidos, entry_email, entry_password, entry_especialidad, entry_turno = entries

        btn_registrar = tk.Button(ventana_registro, text="Registrar", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=registrar)
        btn_registrar.grid(row=len(labels), columnspan=2, pady=20)

    def registrar_enfermero():
        ventana_registro = tk.Toplevel(ventana_principal)
        ventana_registro.title("Registro de Enfermero")
        ventana_registro.geometry("400x400")

        labels = ["Nombre:", "Apellidos:", "Email:", "Contraseña:", "Área:", "Turno:"]
        entries = []

        for i, label_text in enumerate(labels):
            label = tk.Label(ventana_registro, text=label_text, font=("Arial", 12), bg="white", fg="black")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(ventana_registro, font=("Arial", 12), bg="white", fg="black", width=30, show="*" if "Contraseña" in label_text else None)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry.bind("<Enter>", on_enter)
            entry.bind("<Leave>", on_leave)
            entries.append(entry)

        def registrar():
            nombre = entry_nombre.get()
            apellidos = entry_apellidos.get()
            email = entry_email.get()
            password = entry_password.get()
            area = entry_area.get()
            turno = entry_turno.get()
            obj_enfermero = enfermero.Enfermero(nombre, apellidos, email, password, area, turno)
            if obj_enfermero.registrar():
                messagebox.showinfo("Éxito", f"{nombre} {apellidos}, se registró correctamente, con el email {email}")
            else:
                messagebox.showerror("Error", "No fue posible registrar el enfermero. Inténtelo de nuevo más tarde.")
            ventana_registro.destroy()

        entry_nombre, entry_apellidos, entry_email, entry_password, entry_area, entry_turno = entries

        btn_registrar = tk.Button(ventana_registro, text="Registrar", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=registrar)
        btn_registrar.grid(row=len(labels), columnspan=2, pady=20)

    def login_medico():
        ventana_login = tk.Toplevel(ventana_principal)
        ventana_login.title("Login Médico")
        ventana_login.geometry("400x300")

        labels = ["Email:", "Contraseña:"]
        entries = []

        for i, label_text in enumerate(labels):
            label = tk.Label(ventana_login, text=label_text, font=("Arial", 12), bg="white", fg="black")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(ventana_login, font=("Arial", 12), bg="white", fg="black", width=30, show="*" if "Contraseña" in label_text else None)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry.bind("<Enter>", on_enter)
            entry.bind("<Leave>", on_leave)
            entries.append(entry)

        def login():
            email = entry_email.get()
            password = entry_password.get()
            registro = medico.Medico.iniciar_sesion(email, password)
            if registro:
                menu_medico(registro)
            else:
                messagebox.showerror("Error", "Email o contraseña incorrectos. Inténtelo de nuevo.")

        entry_email, entry_password = entries

        btn_login = tk.Button(ventana_login, text="Login", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=login)
        btn_login.grid(row=len(labels), columnspan=2, pady=20)

    def login_enfermero():
        ventana_login = tk.Toplevel(ventana_principal)
        ventana_login.title("Login Enfermero")
        ventana_login.geometry("400x300")

        labels = ["Email:", "Contraseña:"]
        entries = []

        for i, label_text in enumerate(labels):
            label = tk.Label(ventana_login, text=label_text, font=("Arial", 12), bg="white", fg="black")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(ventana_login, font=("Arial", 12), bg="white", fg="black", width=30, show="*" if "Contraseña" in label_text else None)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry.bind("<Enter>", on_enter)
            entry.bind("<Leave>", on_leave)
            entries.append(entry)

        def login():
            email = entry_email.get()
            password = entry_password.get()
            registro = enfermero.Enfermero.iniciar_sesion(email, password)
            if registro:
                menu_enfermero(registro)
            else:
                messagebox.showerror("Error", "Email o contraseña incorrectos. Inténtelo de nuevo.")

        entry_email, entry_password = entries

        btn_login = tk.Button(ventana_login, text="Login", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=login)
        btn_login.grid(row=len(labels), columnspan=2, pady=20)

    def menu_medico(medico_tuple):
        ventana_menu = tk.Toplevel(ventana_principal)
        ventana_menu.title("Menú Médico")
        ventana_menu.geometry("500x400")

        tk.Label(ventana_menu, text=f"Bienvenido(a) {medico_tuple[1]} {medico_tuple[2]}", font=("Arial", 18)).pack(pady=20)

        def registrar_paciente():
            ventana_registro = tk.Toplevel(ventana_menu)
            ventana_registro.title("Registrar Paciente")
            ventana_registro.geometry("400x400")

            labels = ["Nombre:", "Edad:", "Sexo:", "Tipo de sangre:", "Altura:", "Peso:", "Alergias:", "Número de cama:", "ID Médico:", "ID Enfermero:"]
            entries = []

            for i, label_text in enumerate(labels):
                label = tk.Label(ventana_registro, text=label_text, font=("Arial", 12), bg="white", fg="black")
                label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
                entry = tk.Entry(ventana_registro, font=("Arial", 12), bg="white", fg="black", width=30)
                entry.grid(row=i, column=1, padx=10, pady=5)
                entry.bind("<Enter>", on_enter)
                entry.bind("<Leave>", on_leave)
                entries.append(entry)

            def registrar():
                nombre = entry_nombre.get()
                edad = entry_edad.get()
                sexo = entry_sexo.get()
                tipo_sangre = entry_tipo_sangre.get()
                altura = entry_altura.get()
                peso = entry_peso.get()
                alergias = entry_alergias.get()
                numero_cama = entry_numero_cama.get()
                id_medico = entry_id_medico.get()
                id_enfermero = entry_id_enfermero.get()
                paciente_nuevo = paciente.Paciente(nombre, edad, sexo, tipo_sangre, altura, peso, alergias, numero_cama, id_medico, id_enfermero)
                if paciente_nuevo.registrar():
                    messagebox.showinfo("Éxito", "Paciente registrado correctamente.")
                else:
                    messagebox.showerror("Error", "No fue posible registrar al paciente. Inténtelo de nuevo.")
                ventana_registro.destroy()

            entry_nombre, entry_edad, entry_sexo, entry_tipo_sangre, entry_altura, entry_peso, entry_alergias, entry_numero_cama, entry_id_medico, entry_id_enfermero = entries

            btn_registrar = tk.Button(ventana_registro, text="Registrar", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=registrar)
            btn_registrar.grid(row=len(labels), columnspan=2, pady=20)

        def registrar_diagnostico_y_receta():
            ventana_registro = tk.Toplevel(ventana_menu)
            ventana_registro.title("Registrar Diagnóstico y Receta")
            ventana_registro.geometry("400x300")

            labels = ["ID Paciente:", "Diagnóstico:", "Receta:"]
            entries = []

            for i, label_text in enumerate(labels):
                label = tk.Label(ventana_registro, text=label_text, font=("Arial", 12), bg="white", fg="black")
                label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
                entry = tk.Entry(ventana_registro, font=("Arial", 12), bg="white", fg="black", width=30)
                entry.grid(row=i, column=1, padx=10, pady=5)
                entry.bind("<Enter>", on_enter)
                entry.bind("<Leave>", on_leave)
                entries.append(entry)

            def registrar():
                id_paciente = entry_id_paciente.get()
                diagnostico = entry_diagnostico.get()
                receta = entry_receta.get()
                if medico_tuple[0].registrar_diagnostico(id_paciente, diagnostico, receta):
                    messagebox.showinfo("Éxito", "Diagnóstico y receta registrados correctamente.")
                else:
                    messagebox.showerror("Error", "No fue posible registrar el diagnóstico y la receta. Inténtelo de nuevo.")
                ventana_registro.destroy()

            entry_id_paciente, entry_diagnostico, entry_receta = entries

            btn_registrar = tk.Button(ventana_registro, text="Registrar", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=registrar)
            btn_registrar.grid(row=len(labels), columnspan=2, pady=20)

        def ver_paciente():
            ventana_ver = tk.Toplevel(ventana_menu)
            ventana_ver.title("Ver Paciente")
            ventana_ver.geometry("400x400")

            label_id_paciente = tk.Label(ventana_ver, text="ID del Paciente:", font=("Arial", 12), bg="white", fg="black")
            label_id_paciente.grid(row=0, column=0, padx=10, pady=10, sticky="e")
            entry_id_paciente = tk.Entry(ventana_ver, font=("Arial", 12), bg="white", fg="black", width=30)
            entry_id_paciente.grid(row=0, column=1, padx=10, pady=10)
            entry_id_paciente.bind("<Enter>", on_enter)
            entry_id_paciente.bind("<Leave>", on_leave)

            def ver():
                id_paciente = entry_id_paciente.get()
                paciente_info = paciente.Paciente.obtener(id_paciente)
                if paciente_info:
                    messagebox.showinfo("Información del Paciente", f"""
                    Nombre: {paciente_info[1]}
                    Edad: {paciente_info[2]}
                    Sexo: {paciente_info[3]}
                    Tipo de Sangre: {paciente_info[4]}
                    Altura: {paciente_info[5]}
                    Peso: {paciente_info[6]}
                    Alergias: {paciente_info[7]}
                    Número de Cama: {paciente_info[8]}
                    Médico atendió: {paciente_info[9]}
                    Enfermero que atendió: {paciente_info[10]}
                    Fecha de Registro: {paciente_info[11]}
                    """)
                else:
                    messagebox.showerror("Error", "Paciente no encontrado.")

            btn_ver = tk.Button(ventana_ver, text="Ver Paciente", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=ver)
            btn_ver.grid(row=1, columnspan=2, pady=20)

        tk.Button(ventana_menu, text="Registrar Paciente", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=registrar_paciente).pack(pady=10)
        tk.Button(ventana_menu, text="Registrar Diagnóstico y Receta", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=registrar_diagnostico_y_receta).pack(pady=10)
        tk.Button(ventana_menu, text="Ver Paciente", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=ver_paciente).pack(pady=10)
        tk.Button(ventana_menu, text="Cerrar Sesión", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=ventana_menu.destroy).pack(pady=10)

    def menu_enfermero(enfermero_tuple):
        ventana_menu = tk.Toplevel(ventana_principal)
        ventana_menu.title("Menú Enfermero")
        ventana_menu.geometry("500x400")

        tk.Label(ventana_menu, text=f"Bienvenido(a) {enfermero_tuple[1]} {enfermero_tuple[2]}", font=("Arial", 18)).pack(pady=20)

        def registrar_paciente():
            ventana_registro = tk.Toplevel(ventana_menu)
            ventana_registro.title("Registrar Paciente")
            ventana_registro.geometry("400x400")

            labels = ["Nombre:", "Edad:", "Sexo:", "Tipo de sangre:", "Altura:", "Peso:", "Alergias:", "Número de cama:", "ID Médico:", "ID Enfermero:"]
            entries = []

            for i, label_text in enumerate(labels):
                label = tk.Label(ventana_registro, text=label_text, font=("Arial", 12), bg="white", fg="black")
                label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
                entry = tk.Entry(ventana_registro, font=("Arial", 12), bg="white", fg="black", width=30)
                entry.grid(row=i, column=1, padx=10, pady=5)
                entry.bind("<Enter>", on_enter)
                entry.bind("<Leave>", on_leave)
                entries.append(entry)

            def registrar():
                nombre = entry_nombre.get()
                edad = entry_edad.get()
                sexo = entry_sexo.get()
                tipo_sangre = entry_tipo_sangre.get()
                altura = entry_altura.get()
                peso = entry_peso.get()
                alergias = entry_alergias.get()
                numero_cama = entry_numero_cama.get()
                id_medico = entry_id_medico.get()
                id_enfermero = entry_id_enfermero.get()
                paciente_nuevo = paciente.Paciente(nombre, edad, sexo, tipo_sangre, altura, peso, alergias, numero_cama, id_medico, id_enfermero)
                if paciente_nuevo.registrar():
                    messagebox.showinfo("Éxito", "Paciente registrado correctamente.")
                else:
                    messagebox.showerror("Error", "No fue posible registrar al paciente. Inténtelo de nuevo.")
                ventana_registro.destroy()

            entry_nombre, entry_edad, entry_sexo, entry_tipo_sangre, entry_altura, entry_peso, entry_alergias, entry_numero_cama, entry_id_medico, entry_id_enfermero = entries

            btn_registrar = tk.Button(ventana_registro, text="Registrar", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=registrar)
            btn_registrar.grid(row=len(labels), columnspan=2, pady=20)

        def registrar_signos_vitales():
            ventana_registro = tk.Toplevel(ventana_menu)
            ventana_registro.title("Registrar Signos Vitales")
            ventana_registro.geometry("400x300")

            labels = ["ID Paciente:", "Temperatura:", "Presión Sistólica:", "Presión Diastólica:", "Pulso:"]
            entries = []

            for i, label_text in enumerate(labels):
                label = tk.Label(ventana_registro, text=label_text, font=("Arial", 12), bg="white", fg="black")
                label.grid(row=i, column=0, padx=10, pady=5                , sticky="e")
                entry = tk.Entry(ventana_registro, font=("Arial", 12), bg="white", fg="black", width=30)
                entry.grid(row=i, column=1, padx=10, pady=5)
                entry.bind("<Enter>", on_enter)
                entry.bind("<Leave>", on_leave)
                entries.append(entry)

            def registrar():
                id_paciente = entry_id_paciente.get()
                temperatura = entry_temperatura.get()
                presion_sistolica = entry_presion_sistolica.get()
                presion_diastolica = entry_presion_diastolica.get()
                pulso = entry_pulso.get()
                if paciente.Paciente.registrar_signos_vitales(id_paciente, temperatura, presion_sistolica, presion_diastolica, pulso):
                    messagebox.showinfo("Éxito", "Signos vitales registrados correctamente.")
                else:
                    messagebox.showerror("Error", "No fue posible registrar los signos vitales. Inténtelo de nuevo.")
                ventana_registro.destroy()

            entry_id_paciente, entry_temperatura, entry_presion_sistolica, entry_presion_diastolica, entry_pulso = entries

            btn_registrar = tk.Button(ventana_registro, text="Registrar", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=registrar)
            btn_registrar.grid(row=len(labels), columnspan=2, pady=20)

        tk.Button(ventana_menu, text="Registrar Paciente", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=registrar_paciente).pack(pady=10)
        tk.Button(ventana_menu, text="Registrar Signos Vitales", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=registrar_signos_vitales).pack(pady=10)
        tk.Button(ventana_menu, text="Cerrar Sesión", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=ventana_menu.destroy).pack(pady=10)

    # Interfaz principal
    tk.Label(ventana_principal, text="Bienvenido al Sistema de Gestión Hospitalaria", font=("Arial", 18)).pack(pady=20)
    
    tk.Button(ventana_principal, text="Login Médico", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=login_medico).pack(pady=10)
    tk.Button(ventana_principal, text="Login Enfermero", font=("Arial", 12, "bold"), bg="black", fg="white", width=20, command=login_enfermero).pack(pady=10)

    ventana_principal.mainloop()

if __name__ == "__main__":
    menu_principal()
