import { Component, OnInit } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, FormGroup, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { EmployeeService } from '../../services/employee.service';
import { Employee } from '../../models/employee';

@Component({
  selector: 'app-employee-form',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './employee-form.component.html',
  styleUrls: ['./employee-form.component.css']
})
export class EmployeeFormComponent implements OnInit {
  employeeForm!: FormGroup;
  editing = false;

  constructor(private fb: FormBuilder, private employeeService: EmployeeService) {}

  ngOnInit(): void {
    this.employeeForm = this.fb.group({
      id: [null],
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      position: ['', Validators.required],
      departmentId: [null, [Validators.required, Validators.min(1)]],
      hireDate: ['', Validators.required],
    });
  }

  onSubmit(): void {
    const employee: Employee = this.employeeForm.value;

    this.employeeService.save(employee).subscribe({
      next: () => {
        alert(this.editing ? 'Employee updated' : 'Employee added');
        this.employeeForm.reset();
        this.editing = false;
      },
      error: err => console.error(err)
    });
  }

  loadEmployee(id: number): void {
    this.employeeService.getById(id).subscribe({
      next: employee => {
        this.employeeForm.patchValue(employee);
        this.editing = true;
      },
      error: err => alert('Employee not found')
    });
  }

  deleteEmployee(id: number): void {
    if (confirm('Are you sure you want to delete this employee?')) {
      this.employeeService.delete(id).subscribe({
        next: () => {
          alert('Employee deleted');
          if (this.employeeForm.value.id == id) {
            this.employeeForm.reset();
            this.editing = false;
          }
        },
        error: err => console.error(err)
      });
    }
  }
}
