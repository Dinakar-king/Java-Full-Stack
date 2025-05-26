import { Component, OnInit } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, FormGroup, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { DepartmentService } from '../../services/department.service';
import { Department } from '../../models/department';

@Component({
  selector: 'app-department-form',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './department-form.component.html',
  styleUrls: ['./department-form.component.css']
})
export class DepartmentFormComponent implements OnInit {
deletedepartment(arg0: number) {
throw new Error('Method not implemented.');
}
loaddepartment(arg0: number) {
throw new Error('Method not implemented.');
}
  departmentForm!: FormGroup;
  editing = false;

  constructor(private fb: FormBuilder, private departmentService: DepartmentService) {}

  ngOnInit(): void {
    this.departmentForm = this.fb.group({
      id: [null],
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      position: ['', Validators.required],
      departmentId: [null, [Validators.required, Validators.min(1)]],
      hireDate: ['', Validators.required],
    });
  }

  onSubmit(): void {
    const department: Department = this.departmentForm.value;

    this.departmentService.save(department).subscribe({
      next: () => {
        alert(this.editing ? 'Department updated' : 'Department added');
        this.departmentForm.reset();
        this.editing = false;
      },
      error: err => console.error(err)
    });
  }

  loadDepartment(id: number): void {
    this.departmentService.getById(id).subscribe({
      next: department => {
        this.departmentForm.patchValue(department);
        this.editing = true;
      },
      error: err => alert('Department not found')
    });
  }

  deleteDepartment(id: number): void {
    if (confirm('Are you sure you want to delete this department?')) {
      this.departmentService.delete(id).subscribe({
        next: () => {
          alert('Department deleted');
          if (this.departmentForm.value.id == id) {
            this.departmentForm.reset();
            this.editing = false;
          }
        },
        error: err => console.error(err)
      });
    }
  }
}
