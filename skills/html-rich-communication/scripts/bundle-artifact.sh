#!/bin/bash
set -e

echo "📦 Bundling React app to single HTML artifact..."

# Check if we're in a project directory
if [ ! -f "package.json" ]; then
  echo "❌ Error: No package.json found. Run this script from your project root."
  exit 1
fi

# Check if index.html exists
if [ ! -f "index.html" ]; then
  echo "❌ Error: No index.html found in project root."
  echo "   This script requires an index.html entry point."
  exit 1
fi

# Install bundling dependencies
echo "📦 Installing bundling dependencies..."
pnpm add -D parcel @parcel/config-default parcel-resolver-tspaths html-inline

# Parcel pulls native deps; pnpm 10+ blocks their postinstall until approved
echo "🔧 Allowing Parcel native build dependencies..."
node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json', 'utf8'));
const required = ['@parcel/watcher', '@swc/core', 'lmdb', 'msgpackr-extract'];
pkg.pnpm = pkg.pnpm || {};
const existing = pkg.pnpm.onlyBuiltDependencies || [];
pkg.pnpm.onlyBuiltDependencies = [...new Set([...existing, ...required])];
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2) + '\n');
"
pnpm install

# Ensure tsconfig paths exist for parcel-resolver-tspaths
if [ -f "tsconfig.json" ]; then
  node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json', 'utf8'));
const config = JSON.parse(fs.readFileSync('tsconfig.json', 'utf8'));
config.compilerOptions = config.compilerOptions || {};
if (!config.compilerOptions.baseUrl) config.compilerOptions.baseUrl = '.';
if (!config.compilerOptions.paths) config.compilerOptions.paths = { '@/*': ['./src/*'] };
fs.writeFileSync('tsconfig.json', JSON.stringify(config, null, 2) + '\n');
"
fi

# Create Parcel config with tspaths resolver
if [ ! -f ".parcelrc" ]; then
  echo "🔧 Creating Parcel configuration with path alias support..."
  cat > .parcelrc << 'EOF'
{
  "extends": "@parcel/config-default",
  "resolvers": ["parcel-resolver-tspaths", "..."]
}
EOF
fi

# Clean previous build
echo "🧹 Cleaning previous build..."
rm -rf dist bundle.html .parcel-cache

# Build with Parcel
echo "🔨 Building with Parcel..."
pnpm exec parcel build index.html --dist-dir dist --no-source-maps

# Inline everything into single HTML
echo "🎯 Inlining all assets into single HTML file..."
pnpm exec html-inline dist/index.html > bundle.html

# Get file size
FILE_SIZE=$(du -h bundle.html | cut -f1)

echo ""
echo "✅ Bundle complete!"
echo "📄 Output: bundle.html ($FILE_SIZE)"
echo ""
echo "Copy to the working folder deliverable:"
echo "  cp bundle.html ../final/bundle.html"
echo ""
echo "Then run browser verification (step 8) before reporting completion."
