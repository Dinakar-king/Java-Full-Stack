import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './components/header/header.component';
import { DepartmentComponent } from "./components/department/department.component";


@Component({
  selector: 'app-root',
  imports: [RouterOutlet, HeaderComponent, DepartmentComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'employee_management';
}
