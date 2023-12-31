import { NavLink } from 'react-router-dom'
import c from './nav.module.scss'
const Nav = () => {
  return (
    <>
      <nav className={c.nav}>
        <ul>
          <li>
            <NavLink
              to={`/`}
              className={({ isActive }) => (isActive ? c.active : '')}
            >
              Home
            </NavLink>
          </li>
          <li>
            <NavLink
              to={`/schedule`}
              className={({ isActive }) => (isActive ? c.active : '')}
            >
              Schedule
            </NavLink>
          </li>
          <li>
            <NavLink
              to={`/tasks`}
              className={({ isActive }) => (isActive ? c.active : '')}
            >
              Tasks
            </NavLink>
          </li>
        </ul>
      </nav>
    </>
  )
}
export default Nav
