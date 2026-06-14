# Clean line-art SVG icons for each role. Use currentColor so we tint via CSS.
# viewBox 0 0 24 24, stroke-based, 1.8 weight, rounded.

def _wrap(paths):
    return ('<svg class="role-svg" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">' + paths + '</svg>')

ROLE_ICONS = {
    # Frontend ... browser window + cursor
    "frontend": _wrap(
        '<rect x="3" y="4" width="18" height="14" rx="2"/>'
        '<path d="M3 8h18"/><circle cx="6" cy="6" r="0.6" fill="currentColor"/>'
        '<path d="M9 21h6M12 18v3"/><path d="m13 12 4 2-2 1-1 2-1-5Z"/>'
    ),
    # Backend ... stacked database/servers
    "backend": _wrap(
        '<ellipse cx="12" cy="5" rx="7" ry="2.5"/>'
        '<path d="M5 5v6c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5V5"/>'
        '<path d="M5 11v6c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5v-6"/>'
    ),
    # Data Scientist ... scatter chart with trend
    "data-scientist": _wrap(
        '<path d="M4 4v16h16"/><path d="m7 15 3-4 3 2 4-6"/>'
        '<circle cx="7" cy="15" r="0.9" fill="currentColor"/>'
        '<circle cx="10" cy="11" r="0.9" fill="currentColor"/>'
        '<circle cx="13" cy="13" r="0.9" fill="currentColor"/>'
        '<circle cx="17" cy="7" r="0.9" fill="currentColor"/>'
    ),
    # AI/ML ... neural network nodes
    "ai-ml": _wrap(
        '<circle cx="5" cy="6" r="1.6"/><circle cx="5" cy="18" r="1.6"/>'
        '<circle cx="12" cy="12" r="1.8"/>'
        '<circle cx="19" cy="6" r="1.6"/><circle cx="19" cy="18" r="1.6"/>'
        '<path d="M6.4 6.8 10.4 11M6.4 17.2 10.4 13M13.6 11 17.6 6.8M13.6 13 17.6 17.2"/>'
    ),
    # PM ... clipboard/checklist + flag
    "pm": _wrap(
        '<rect x="5" y="4" width="14" height="17" rx="2"/>'
        '<path d="M9 4V3h6v1"/><path d="m8 10 1.5 1.5L12 9"/>'
        '<path d="M14 10.5h3M8 15h8"/>'
    ),
    # Designer ... pen nib / vector
    "designer": _wrap(
        '<path d="M12 3 5 10l-1.5 6.5L10 15l7-7Z"/>'
        '<path d="m10 15-2.5 2.5"/><circle cx="13.5" cy="6.5" r="1.1"/>'
    ),
    # DevOps/SRE ... infinity loop / cycle
    "devops": _wrap(
        '<path d="M7 8a4 4 0 1 0 0 8c2 0 3-1.5 5-4s3-4 5-4a4 4 0 1 1 0 8c-2 0-3-1.5-5-4"/>'
    ),
    # Data Engineer ... pipeline / connected pipes
    "data-engineer": _wrap(
        '<rect x="3" y="5" width="5" height="5" rx="1"/>'
        '<rect x="16" y="14" width="5" height="5" rx="1"/>'
        '<path d="M8 7.5h4a2 2 0 0 1 2 2v5a2 2 0 0 0 2 2"/>'
        '<path d="M5.5 10v3.5a2 2 0 0 0 2 2H10"/>'
    ),
    # EM/Leader ... people / org chart
    "em": _wrap(
        '<circle cx="12" cy="6" r="2.2"/>'
        '<circle cx="6" cy="17" r="2.2"/><circle cx="18" cy="17" r="2.2"/>'
        '<path d="M12 8.2v3M12 11.2H6.2v3.6M12 11.2h5.8v3.6"/>'
    ),
}
