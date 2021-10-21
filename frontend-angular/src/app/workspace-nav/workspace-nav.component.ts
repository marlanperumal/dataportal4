import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-workspace-nav',
  templateUrl: './workspace-nav.component.html',
  styleUrls: ['./workspace-nav.component.scss']
})
export class WorkspaceNavComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  workspaces = ['Workspace 1', 'Workspace 2'];
  activeWorkspace = this.workspaces[0];

  addWorkspace() {
    const newWorkspace = `Workspace ${this.workspaces.length + 1}`;
    this.workspaces.push(newWorkspace);
    this.activeWorkspace = newWorkspace;
  }

  selectWorkspace(workspace: string) {
    this.activeWorkspace = workspace;
  }
}
