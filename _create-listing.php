<?php

$output        = 'README.md';
$per_row       = 10;
$files         = glob('emoji/*.{png,gif,jpg,jpeg}', GLOB_BRACE);
$listing       = [];
$per_row_width = floor(100 / $per_row) . '%';

sort($files);

if (count($files) < 1) {
    die('No images to continue with.');
}

function get_basename(string $file)
{
    $parts = explode(DIRECTORY_SEPARATOR, $file);
    return end($parts);
}

foreach ($files as $file) {
    $first = get_basename($file);
    $first = str_replace('emoji/', '', $first);
    $first = trim($first[0]);

    if (preg_match('/([^a-zA-Z:])/', $first)) {
        $first = '\[^a-zA-Z:\]';
    }

    if (!array_key_exists($first, $listing)) {
        $listing[$first] = [];
    }

    $listing[$first][] = $file;
}

$contents = "# Emotes\n\n";

foreach ($listing as $header => $icons) {
    $contents .= sprintf("## %s\n\n", $header);

    $chunks = array_chunk($icons, $per_row);

    $contents .= '<table style="text-align: center;width: 100%">' . "\n";

    foreach ($chunks as $chunk_icons) {
        $contents .= "<tr>\n";

        foreach ($chunk_icons as $icon) {
            $file = $icon;
            [$name, $ext] = explode('.', get_basename($icon), 2);

            $format   = '<td style=\'width: %s\'><img width=\'30\' src="%2$s"'
                . ' alt="%2$s" title=":%3$s:"></td>';
            $contents .= sprintf($format, $per_row_width, $file, $name) . "\n";
        }

        $contents .= "</tr>\n";
    }

    $contents .= "</table>\n\n";
}

$contents .= "\n\n Generated: " . date('c');

file_put_contents($output, $contents);
