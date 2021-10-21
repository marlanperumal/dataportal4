import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-new-workspace',
  templateUrl: './new-workspace.component.html',
  styleUrls: ['./new-workspace.component.scss']
})
export class NewWorkspaceComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  options = [
    "Quick Analysis",
    "New Dashboard",
    "Open Workspace",
    "Import Own Data",
    "Manage Own Data",
    "Subscribe to Data",
  ]

}
