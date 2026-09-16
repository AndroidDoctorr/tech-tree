# Repoint v1-relative markdown links at their v2 equivalents.
# Run from repo root. Use -Apply to write; default is a dry run.
param([switch]$Apply, [switch]$Journal)

$v2 = Join-Path (Get-Location) 'v2'

# logical v1 path -> v2-root-relative path
$map = @{
    'player-calendar.md'             = 'checklists/calendar.md'
    'routines.md'                    = 'checklists/index.md'
    'rules.md'                       = 'player-introduction.md'
    'purpose.md'                     = 'overview.md'
    'inventory.md'                   = 'inventory/index.md'
    'inventory/bridges-and-trail.md' = 'map/region/trails-and-bridges.md'
    'inventory/tools-lab.md'         = 'inventory/tools.md'
    'inventory/fixtures.md'          = 'inventory/infrastructure.md'
    'route-a-road.md'                = 'map/region/trails-and-bridges.md'
    'resource-map.md'                = 'map/region/resources.md'
    'map.md'                         = 'map/index.md'
    'bees.md'                        = 'government/procedures/bees.md'
    'museum.md'                      = 'inventory/museum.md'
    'building-code-1.md'             = 'government/regulations/building-code-1.md'
    'storage-code-1.md'              = 'government/regulations/storage-code-1.md'
    'house-plan.md'                  = 'government/archive/house-plan.md'
    'chem-lab-plan.md'               = 'government/archive/chem-lab-plan.md'
    'craft-wing-plan.md'             = 'government/archive/craft-wing-plan.md'
    'obsolete/ladder.md'             = 'government/archive/ladder.md'
    'obsolete/schedule.md'           = 'government/archive/schedule.md'
    'now.md'                         = 'now.md'
    'skills.md'                      = 'player-introduction.md'
    'food-menu.md'                   = 'government/procedures/food-menu.md'
    'linens-grammar.md'              = 'government/procedures/linens-grammar.md'
    'trail-longevity.md'             = 'government/procedures/trail-longevity.md'
    'furniture-code-1.md'            = 'government/regulations/furniture-code-1.md'
    'crop-selection-improvement-manual-1.md' = 'government/regulations/crop-selection-improvement-code-1.md'
    'crop-selection-improvement-code-1.md'   = 'government/regulations/crop-selection-improvement-code-1.md'
    'campus-waste-drainage-manual-1.md'      = 'government/regulations/waste-management-drainage-code-1.md'
    'waste-management-drainage-code-1.md'    = 'government/regulations/waste-management-drainage-code-1.md'
    'ladder.md'                      = 'government/archive/ladder.md'
    'schedule.md'                    = 'government/archive/schedule.md'
    'advancements.md'                = 'government/archive/advancements.md'
    'materials-roadmap.md'           = 'government/archive/materials-roadmap.md'
    'year-001-plan.md'               = 'government/archive/year-001-plan.md'
    'year-002-plan.md'               = 'government/archive/year-002-plan.md'
    'route-nomenclature.md'          = 'government/archive/route-nomenclature.md'
    'ore-trip-gps-notes.md'          = 'government/archive/ore-trip-gps-notes.md'
    'sun-calendar.md'                = 'checklists/calendar.md'
    'hazards.md'                     = 'hazards.md'
    'journal/index.md'               = 'journal/index.md'
}

# files whose links are correct relative to themselves, not to v2 root
$local = @{
    'map\index.md'       = @{ 'campus.md' = 'campus/index.md'; 'domus.md' = 'campus/domus.md'; 'region.md' = 'region/index.md' }
    'inventory\index.md' = @{ 'infrastrucutre.md' = 'infrastructure.md'; 'atelier.mc' = 'atelier.md' }
}

$files = Get-ChildItem $v2 -Recurse -File -Filter *.md |
    Where-Object { $_.FullName -notmatch '\\archive\\' }
if (-not $Journal) {
    $files = $files | Where-Object { $_.FullName -notmatch '\\journal\\(days|weeks|summaries)\\' }
}

# Basename -> v2-relative path, for journal files only, and only where the basename
# is unique. Repairs day/week links written before the year-NNN folder split.
$byName = @{}
foreach ($j in Get-ChildItem (Join-Path $v2 'journal') -Recurse -File -Filter *.md) {
    $n = $j.Name
    if ($byName.ContainsKey($n)) { $byName[$n] = $null }
    else { $byName[$n] = ($j.FullName.Substring($v2.Length + 1) -replace '\\', '/') }
}

$changed = 0
$fixed = 0

foreach ($f in $files) {
    $rel = $f.FullName.Substring($v2.Length + 1)
    $depth = ($rel -split '\\').Count - 1
    $prefix = '../' * $depth
    $text = Get-Content $f.FullName -Raw
    if ([string]::IsNullOrEmpty($text)) { continue }
    $orig = $text

    foreach ($m in [regex]::Matches($orig, '\]\(([^)#][^)]*\.md)\)')) {
        $target = $m.Groups[1].Value
        if (Test-Path (Join-Path $f.DirectoryName $target)) { continue }

        $new = $null
        if ($local.ContainsKey($rel) -and $local[$rel].ContainsKey($target)) {
            $new = $local[$rel][$target]
        }
        else {
            $logical = $target -replace '^(\.\./)+', ''
            if ($map.ContainsKey($logical)) { $new = $prefix + $map[$logical] }
            elseif ($logical -match '^journal/days/') { $new = $prefix + $logical }
            else {
                $base = Split-Path $target -Leaf
                if ($byName.ContainsKey($base) -and $byName[$base]) { $new = $prefix + $byName[$base] }
            }
        }

        if ($new -and $new -ne $target) {
            $text = $text.Replace("]($target)", "]($new)")
            Write-Host ("  {0}`n    {1}  ->  {2}" -f $rel, $target, $new)
            $fixed++
        }
    }

    if ($text -ne $orig) {
        $changed++
        if ($Apply) { Set-Content -Path $f.FullName -Value $text -NoNewline }
    }
}

$verb = if ($Apply) { 'rewrote' } else { 'would rewrite' }
Write-Host ("`n{0} {1} files, repointing {2} links" -f $verb, $changed, $fixed)
